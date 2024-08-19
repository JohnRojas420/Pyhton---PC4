# Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones, también puede usar un 
# menú para organizar su programa):
# - Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar
#  de ese número, donde n es el número introducido.
# - Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
#  donde “n” es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje 
# por pantalla informando de ello.
# - Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
#  y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla 
# informando de ello.

#Solución:
#Se importa la librería OS
import os

class TablaMultiplicar:
    @staticmethod
    def crear_tabla(n):
        with open(f'tabla-{n}.txt', 'w') as f:
            for i in range(1, 11):
                f.write(f'{n} x {i} = {n * i}\n')
        print(f'Tabla del {n} guardada en tabla-{n}.txt')

    @staticmethod
    def mostrar_tabla(n): 
        try:
            with open(f'tabla-{n}.txt', 'r') as f:
                print(f'Contenido de tabla-{n}.txt:')
                print(f.read())
        except FileNotFoundError:
            print(f'El fichero tabla-{n}.txt no existe.')

    @staticmethod
    def mostrar_linea(n, m):
        try:
            with open(f'tabla-{n}.txt', 'r') as f:
                lineas = f.readlines()
                if 1 <= m <= 10:
                    print(f'Línea {m} de tabla-{n}.txt:')
                    print(lineas[m-1].strip())
                else:
                    print('El número m debe estar entre 1 y 10.')
        except FileNotFoundError:
            print(f'El fichero tabla-{n}.txt no existe.')
        except IndexError:
            print(f'El número m está fuera del rango de la tabla.')
#Definiendo el menú(Crear,Mostrar tabla, Línea de tabla y Salir)
def menu():
    while True:
        print("\nMenú:")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                TablaMultiplicar.crear_tabla(n)
            else:
                print("Número fuera de rango.")

        elif opcion == '2':
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                TablaMultiplicar.mostrar_tabla(n)
            else:
                print("Número fuera de rango.")

        elif opcion == '3':
            n = int(input("Ingrese el número de la tabla (1-10): "))
            if 1 <= n <= 10:
                m = int(input(f"Ingrese la línea de la tabla {n} (1-10): "))
                TablaMultiplicar.mostrar_linea(n, m)
            else:
                print("Número fuera de rango.")

        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
