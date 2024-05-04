import matplotlib.pyplot as plt

# Datos de ejemplo: horas y temperaturas
horas = list(range(24))  # 24 horas del día
temperaturas = [20, 19, 18, 17, 16, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31, 30, 29, 28]

# Definir los rangos de temperatura y los colores correspondientes
rango_bajo = 18
rango_alto = 30
colores = ['blue' if temp < rango_bajo else 'green' if rango_bajo <= temp <= rango_alto else 'red' for temp in temperaturas]

# Crear un nuevo gráfico
plt.figure(figsize=(10, 6))

# Graficar las temperaturas con barras verticales de colores
plt.bar(horas, temperaturas, color=colores)

# Etiquetas y título
plt.xlabel('Hora del día')
plt.ylabel('Temperatura (°C)')
plt.title('Variación de la temperatura durante un día')

# Guardar el gráfico como una imagen sin mostrarla
plt.savefig('temperaturas_dia.png')

# Cerrar la figura para evitar que se muestre
plt.close()