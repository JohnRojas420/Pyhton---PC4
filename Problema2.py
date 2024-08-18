# Cree un programa el cual cumpla con las siguientes especificaciones:
# - Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
# fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
# - Solicite al usuario un texto.
# - Finalmente, su programa deberá imprimir el texto solicitado usando la fuente apropiada.

#Solución

# Se instala la librería "pyfiglet" y se importan:
import pyfiglet
import random
# Se empieza definiendo el texto
def imprimir_texto_con_fuente():
    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = pyfiglet.FigletFont.getFonts()

    # Solicitar al usuario el nombre de la fuente
    fuente = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")

    # Seleccionar una fuente aleatoria si no se ingresa ninguna
    if not fuente:
        fuente = random.choice(fuentes_disponibles)

    # Verificar si la fuente ingresada es válida
    if fuente not in fuentes_disponibles:
        print(f"La fuente '{fuente}' no está disponible. Se seleccionará una fuente aleatoria.")
        fuente = random.choice(fuentes_disponibles)

    # Solicitar al usuario el texto a imprimir
    texto = input("Ingrese el texto a imprimir: ")

    # Generar el texto con la fuente seleccionada
    resultado = pyfiglet.figlet_format(texto, font=fuente)

    # Imprimir el resultado
    print(resultado)
# Ejecutar la función
imprimir_texto_con_fuente()
