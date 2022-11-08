import urllib.parse

import requests
'''main_api - la URL principal a la que está accediendo'''
main_api = "https://www.mapquestapi.com/directions/v2/route?"
'''key: la clave del consumidor de la API de MapQuest que recuperó del sitio web del desarrollador'''
key  = "your_api_key"
print("URL: " + (url))
'''variable que usando el método get para solicitar datos JSON de la URL enviada.'''
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
'''instrucción if que imprima el estado de la solicitud
 si la clave del código de estado se establece en el valor 0.'''
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

'''Vuelva a escribir el origen y el destino para que estén dentro de un ciclo while
 en el que solicita la entrada del usuario para la ubicación inicial y el destino.'''
# The "while true" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    '''declaración if después de la variable de 
    dirección para verificar si el usuario ingresa q o quit.'''
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))
'''impresión que muestren las ubicaciones de origen y destino, 
así como las claves formateadas de tiempo, distancia y lo que utilizo.
'''
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
    '''EL formato "{:.2f}". para dar formato a los valores flotantes con 2 decimales 
    antes de convertirlos en valores de cadena'''
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    print("===================")