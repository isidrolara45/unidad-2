import urllib.parse
'''Importe módulos existentes para agregar funcionalidad '''
import requests
'''main_api - la URL principal '''
main_api = "https://www.mapquestapi.com/directions/v2/route?"
'''key: la clave del consumidor de la API de MapQuest que recuperó del sitio web del desarrollador'''
key  = "your_api_key"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))
'''Cree una variable que usando el método get para solicitar datos JSON de la URL enviada.'''
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
    '''declaración if después de la variable de dirección para verificar si el usuario ingresa o quit.'''
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
    print("Miles:           " + str(json_data["route"]["distance"]))
    print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
    print("======================")