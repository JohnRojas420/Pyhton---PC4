#Empleando el ejercicio visto en clase de Procesamiento con Ficheros. Supongamos que el precio brindado en el
# archivo “ventas.csv” ha sido dato en dolares. Deberá solarizar el precio según la fecha de compra, para esto 
#deberá leer la información almacenada de tipo de cambio de la base mongodb o sqlite (elegir una).
# Finalmente mostrar el precio total en dolares y soles por cada producto

#Solución:

import csv
import sqlite3

def leer_ventas(archivo):
    ventas = []
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ventas.append({
                'producto': row['producto'],
                'fecha': row['fecha'],
                'precio_dolar': float(row['precio_dolar'])
            })
    return ventas

def obtener_tipo_cambio_sqlite(fecha):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT compra, venta FROM sunat_info WHERE fecha = ?', (fecha,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[1]  # Devolvemos el tipo de cambio de venta
    else:
        return None
 #Convertir en soles o solarizar:
def solarizar_precios(ventas):
    ventas_solarizadas = []
    for venta in ventas:
        tipo_cambio = obtener_tipo_cambio_sqlite(venta['fecha'])
        if tipo_cambio:
            precio_soles = venta['precio_dolar'] * tipo_cambio
            ventas_solarizadas.append({
                'producto': venta['producto'],
                'precio_dolar': venta['precio_dolar'],
                'precio_soles': precio_soles
            })
        else:
            print(f"Tipo de cambio no encontrado para la fecha {venta['fecha']}")
    return ventas_solarizadas