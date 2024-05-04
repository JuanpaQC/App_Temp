import random
from datetime import datetime, timedelta

def celsius_a_fahrenheit(celsius):
    return int(celsius * 9/5 + 32)

def generar_temperaturas():
    fecha_inicio = datetime(2024, 4, 20, 0, 0, 0)
    temperatura_data = []

    for dia in range(9):  # 7 días
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

                temperatura_data.append((fecha_actual, hora_actual, temperatura_actual_celsius, temperatura_fahrenheit))

        fecha_inicio += timedelta(days=1)  # Pasar al siguiente día

    return temperatura_data

def guardar_en_archivo(temperatura_data):
    with open('temperaturas.txt', 'w') as file:
        for fecha, hora, temperatura_celsius, temperatura_fahrenheit in temperatura_data:
            file.write(f"{temperatura_celsius} C, {temperatura_fahrenheit} F, {fecha}, {hora}\n")

if __name__ == "__main__":
    temperaturas = generar_temperaturas()
    guardar_en_archivo(temperaturas)