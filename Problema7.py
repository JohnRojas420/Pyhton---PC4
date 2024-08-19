# Emplee el API de SUNAT que corresponda para obtener el precio de compra y venta del dólar durante todo el 2023. 
# Almacene dicha información en base de datos sqlite ‘base.db’ con nombre de tabla sunat_info y en mongo db.
# Finalmente deberá mostrar el contenido de dicha tabla.
# Lee la documentación del API: https://apis.net.pe/api-tipo-cambio.html

#Solución:
#Instalar requests, sqlite3 y pymongo:
import requests
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None