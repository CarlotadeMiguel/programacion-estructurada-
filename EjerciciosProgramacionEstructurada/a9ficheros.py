# Programa para leer y escribir en ficheros

# 1. Escritura inicial en un fichero
with open("ejemplo.txt", "w") as fichero:
    fichero.write("Línea 1: Hola, este es un ejemplo de escritura en un fichero.\n")
    fichero.write("Línea 2: Python facilita el manejo de ficheros.\n")
    fichero.write("Línea 3: Este es el final del fichero.\n")
print("Fichero 'ejemplo.txt' creado y escrito con éxito.")

# 2. Permitir al usuario añadir líneas al fichero
print("\nIntroduce líneas para añadir al fichero (escribe 'SALIR' para terminar):")
with open("ejemplo.txt", "a") as fichero:  # Modo 'a' para añadir al final del fichero
    while True:
        linea = input("Introduce una línea: ")
        if linea.upper() == "SALIR":  # Finaliza si el usuario escribe 'SALIR'
            break
        fichero.write(linea + "\n")
print("Líneas añadidas al fichero con éxito.")

# 3. Lectura completa del fichero
print("\nLeyendo el contenido completo del fichero:")
with open("ejemplo.txt", "r") as fichero:
    contenido = fichero.read()
    print(contenido)

# 4. Recorrido secuencial del fichero línea por línea
print("\nLeyendo el fichero línea por línea:")
with open("ejemplo.txt", "r") as fichero:
    for linea in fichero:
        print(linea.strip())  # Elimina los saltos de línea al final de cada línea

# 5. Simulación de feof (fin de fichero)
print("\nSimulación de feof (fin de fichero):")
with open("ejemplo.txt", "r") as fichero:
    while True:
        linea = fichero.readline()
        if not linea:  # Si no hay más líneas, se alcanza el final del fichero
            break
        print(linea.strip())