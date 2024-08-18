# Generar un programa en Python que realice: 
# - Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad de bitcoins que posee
#  el usuario
# - Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando como separador de miles.

#Solución:

# Se importa la librería "requests" para este ejercicio
import requests
# Se define la obtención de Bitcoins
def obtener_precio_bitcoin():
    # Usaré una API pública para obtener el precio actual del Bitcoin en USD:
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    # Hago uso de la librería instalada "requests"
    respuesta = requests.get(url)
    datos = respuesta.json()
    precio_usd = datos["bpi"]["USD"]["rate_float"]
    return precio_usd

def formato_moneda(valor):
    return f"{valor:,.4f}"

def main():
    # Solicitar al usuario la cantidad de Bitcoins
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    
    # Obtener el precio actual del Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()
    
    # Calculando el valor total en USD:
    valor_total_usd = n * precio_bitcoin
    
    # Mostrando el valor total en USD con el formato requerido:
    print(f"El valor de {n} Bitcoins es: ${formato_moneda(valor_total_usd)} USD")

if __name__ == "__main__":
    main()
