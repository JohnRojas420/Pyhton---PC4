#Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y ruta). Y retorne la 
# cantidad de líneas de código de ese archivo, excluyendo los comentarios y líneas en blanco. Si el usuario ingresa
# una ruta inválida o si el nombre del archivo no termina en .py, su programa no retornará ningún resultado.

#Solución:
#Llamar a la librería "os":
import os

def contar_lineas_codigo(ruta_archivo):
    # Verificar si el archivo existe y tiene la extensión .py
    if os.path.isfile(ruta_archivo) and ruta_archivo.endswith('.py'):
        with open(ruta_archivo, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                # Eliminar espacios en blanco al inicio y final de la línea
                linea = linea.strip()
                # Contar líneas que no están vacías y no son comentarios
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1
            return lineas_codigo
    else:
        return None

# Solicitaando la ruta del archivo al usuario:
ruta_archivo = input("Ingrese la ruta del archivo .py: ")

# Se procede a contar las líneas de código:
resultado = contar_lineas_codigo(ruta_archivo)

# Mostrar el resultado
if resultado is not None:
    print(f"El archivo tiene {resultado} líneas de código (excluyendo comentarios y líneas en blanco).")
else:
    print("La ruta es inválida o el archivo no tiene la extensión .py.")