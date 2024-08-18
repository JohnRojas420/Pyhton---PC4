# Crear un programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
# un código que permita hacer un unzip al archivo zipeado.

#Solución:
#Importando archivos zip y os:

import zipfile
import os

# Definiendo la compresión en archivos zip:
def comprimir_imagen(imagen_ruta, nombre_zip):
    # Creando un archivo ZIP
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        # Agregar la imagen al archivo ZIP
        zipf.write(imagen_ruta, os.path.basename(imagen_ruta))
#Imprimiendo la ruta de la imagen- 
    print(f"La imagen {imagen_ruta} ha sido comprimida en {nombre_zip}")

# Definiendo la ruta de la imagen a comprimir
imagen_ruta = 'ruta/a/tu/imagen.png'
# Nombre del archivo ZIP de salida
nombre_zip = 'imagen_comprimida.zip'

# Ejecutar la función para comprimir la imagen
comprimir_imagen(imagen_ruta, nombre_zip)