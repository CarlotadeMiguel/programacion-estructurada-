import os

print("=== Interacción con el Sistema Operativo ===")

# 1. Obtener el directorio actual
print("\n1. Directorio actual:")
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# 2. Listar archivos y directorios en el directorio actual
print("\n2. Archivos y directorios en el directorio actual:")
contenido = os.listdir(directorio_actual)
for item in contenido:
    print(item)

# 3. Crear un nuevo directorio
nuevo_directorio = "nuevo_directorio"
print(f"\n3. Creando un nuevo directorio llamado '{nuevo_directorio}'...")
if not os.path.exists(nuevo_directorio):
    os.mkdir(nuevo_directorio)
    print(f"Directorio '{nuevo_directorio}' creado.")
else:
    print(f"El directorio '{nuevo_directorio}' ya existe.")

# 4. Cambiar al nuevo directorio
print(f"\n4. Cambiando al directorio '{nuevo_directorio}'...")
os.chdir(nuevo_directorio)
print(f"Ahora estás en: {os.getcwd()}")

# 5. Crear y escribir en un archivo
archivo = "archivo_prueba.txt"
print(f"\n5. Creando y escribiendo en el archivo '{archivo}'...")
with open(archivo, "w") as f:
    f.write("Hola, este es un archivo de prueba.\n")
    f.write("Estamos interactuando con el sistema operativo usando Python.\n")
print(f"Archivo '{archivo}' creado y escrito.")

# 6. Leer el contenido del archivo
print(f"\n6. Leyendo el contenido del archivo '{archivo}':")
with open(archivo, "r") as f:
    contenido_archivo = f.read()
    print(contenido_archivo)

# 7. Volver al directorio anterior
print("\n7. Volviendo al directorio anterior...")
os.chdir("..")
print(f"Ahora estás en: {os.getcwd()}")

# 8. Eliminar el archivo y el directorio creado
print(f"\n8. Eliminando el archivo '{archivo}' y el directorio '{nuevo_directorio}'...")
os.remove(os.path.join(nuevo_directorio, archivo))
os.rmdir(nuevo_directorio)
print(f"Archivo y directorio eliminados.")

# 9. Ejecutar un comando del sistema operativo
print("\n9. Ejecutando un comando del sistema operativo:")
comando = "dir" if os.name == "nt" else "ls"  # 'dir' para Windows, 'ls' para Linux/Mac
os.system(comando)

print("\n=== Fin del programa ===")