# Simulación de respuesta de API   
respuesta_api = {   
    "status": "éxito",   
    "data": [   
        {"id": 1, "nombre": "Libro 1", "precio": 29.99},   
        {"id": 2, "nombre": "Libro 2", "precio": 39.99}   
    ],   
    "paginación": {"total": 2, "página": 1}   
}   
# Procesamiento de datos   
libros = [item["nombre"] for item in respuesta_api["data"]]   
precio_total = sum(item["precio"] for item in respuesta_api["data"])

print (respuesta_api)
print (respuesta_api['data'][1])
print (respuesta_api['data'][1]['precio'])
print (libros[1])
