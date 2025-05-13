import json

with open("config.json", "r") as archivo:   
    configuracion = json.load(archivo)   
    print(configuracion["data"])  