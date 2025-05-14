import os

def renombrar_archivos_en_directorio(directorio):
    try:
        # Cambiar al directorio especificado
        os.chdir(directorio)
        print(f"Directorio actual: {os.getcwd()}")

        # Listar todos los archivos en el directorio
        archivos = os.listdir(directorio)
        print("\nArchivos encontrados:")
        print(archivos)

        # Renombrar cada archivo
        for archivo in archivos:
            # Verificar que sea un archivo (y no un directorio)
            if os.path.isfile(archivo):
                nuevo_nombre = f"a{archivo}"  # Agregar "a" al inicio del nombre
                os.rename(archivo, nuevo_nombre)
                print(f"Renombrado: {archivo} -> {nuevo_nombre}")

        print("\nRenombrado completado.")
    except Exception as e:
        print(f"Error: {e}")

# Solicitar al usuario el directorio
directorio = input("Introduce la ruta del directorio donde deseas renombrar los archivos: ")
renombrar_archivos_en_directorio(directorio)