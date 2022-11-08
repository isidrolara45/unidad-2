import urllib.parse
'''Importe módulos existentes para agregar funcionalidad adicional'''
import requests
'''main_api - la URL principal a la que está accediendo'''
main_api = "https://www.mapquestapi.com/directions/v2/route?"
'''orig - el parámetro para especificar su punto de origen'''
orig = "Washington"
'''dest - el parámetro para especificar su destino'''
dest = "Baltimaore"
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