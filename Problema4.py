# Tienes un fichero temperaturas.txt que contiene registros de temperaturas diarias en formato
# CSV. Cada línea del fichero tiene la siguiente estructura: fecha,temperatura. Debes leer el fichero, calcular 
# la temperatura promedio, la temperatura máxima y la mínima. Finalmente, debes escribir los resultados en un 
# nuevo fichero resumen_temperaturas.txt.
# link_fichero:
# https://github.com/gdelgador/ProgramacionPython202407/blob/main/Modulo4/src/temperaturas.txt

#Solución:

# Se define archivos de entrada y uno de salida para el nuevo fichero:
def procesar_temperaturas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        temperaturas = []
        for linea in f:
            fecha, temp = linea.strip().split(',')
            temperaturas.append(float(temp))

    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    temp_promedio = sum(temperaturas) / len(temperaturas)

#Nuevo fichero de salida
    with open(archivo_salida, 'w') as f:
        f.write(f"Temperatura máxima: {temp_max}°C\n")
        f.write(f"Temperatura mínima: {temp_min}°C\n")
        f.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")

# Uso de la función
procesar_temperaturas('temperaturas.txt', 'resumen_temperaturas.txt')