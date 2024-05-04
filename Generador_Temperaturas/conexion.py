import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
from datetime import datetime, timedelta

# Initialize Firebase
cred = credentials.Certificate("C:\\Users\\jpqca\\OneDrive\\Escritorio\\proyecto\\Credenciales\\Proyecto_Temperatura.json")
app = firebase_admin.initialize_app(cred, name='Temperatura')
db = firestore.client(app=app)

def celsius_a_fahrenheit(celsius):
    return int(celsius * 9/5 + 32)

def generar_temperaturas():
    fecha_inicio = datetime(2024, 4, 20, 0, 0, 0)
    temperatura_data = []

    for dia in range(9):  # 9 días
        for hora in range(24):  # 24 horas
            for minuto in range(0, 60, 15):  # Detecciones cada 15 minutos
                if hora < 5:
                    temperatura_actual_celsius = random.randint(17, 19)  # Noche: 17-20°C
                elif 5 <= hora < 12:
                    temperatura_actual_celsius = random.randint(20, 25)  # Mañana: 20-25°C
                elif 12 <= hora < 16:
                    temperatura_actual_celsius = random.randint(25, 31)  # Mediodía: 22-25°C
                else:
                    temperatura_actual_celsius = random.randint(19, 25)  # Tarde-Noche: 19-22°C

                temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_actual_celsius)
                fecha_actual = fecha_inicio.strftime('%d-%m-%Y')
                hora_actual = f"{hora:02d}:{minuto:02d}:00"

                temperatura_data.append({
                    'celcius': temperatura_actual_celsius,
                    'fahrenheit': temperatura_fahrenheit,
                    'date': fecha_actual,
                    'hour': hora_actual
                })

        fecha_inicio += timedelta(days=1)  # Pasar al siguiente día

    return temperatura_data

def subir_a_firebase(temperatura_data):
    for datos in temperatura_data:
        fecha_actual = datos['date']
        doc_ref = db.collection('App_Temp').document(fecha_actual)
        doc_ref.set({
            u'temperaturas': firestore.ArrayUnion([datos])
        }, merge=True)

if __name__ == "__main__":
    temperaturas = generar_temperaturas()
    subir_a_firebase(temperaturas)
