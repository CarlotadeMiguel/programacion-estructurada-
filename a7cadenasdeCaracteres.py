# Programa para manipular cadenas de caracteres

# Entrada de una cadena
cadena = input("Ingresa una cadena de texto: ")

# 1. Convertir a mayúsculas y minúsculas
print("\nManipulación de cadenas:")
print(f"En mayúsculas: {cadena.upper()}")
print(f"En minúsculas: {cadena.lower()}")

# 2. Contar caracteres
print(f"Número de caracteres: {len(cadena)}")

# 3. Reemplazar palabras caracteres que coinciden si decides cambiar ola en Hola ola saldrá Hole ole 
palabra_a_reemplazar = input("\nIngresa la palabra que deseas reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")
cadena_reemplazada = cadena.replace(palabra_a_reemplazar, nueva_palabra)
print(f"Cadena después del reemplazo: {cadena_reemplazada}")

# 4. Dividir la cadena en palabras
palabras = cadena_reemplazada.split()
print(f"\nLista de palabras: {palabras}")

# 5. Verificar si una palabra está en la cadena
palabra_a_buscar = input("\nIngresa una palabra para buscar en la cadena: ")
if palabra_a_buscar in cadena_reemplazada:
    print(f"La palabra '{palabra_a_buscar}' se encuentra en la cadena.")
else:
    print(f"La palabra '{palabra_a_buscar}' no se encuentra en la cadena.")

# 6. Invertir la cadena
cadena_invertida = cadena_reemplazada[::-1]
print(f"\nCadena invertida: {cadena_invertida}")

# 7. Eliminar espacios al inicio y al final
cadena_sin_espacios = cadena_reemplazada.strip()
print(f"\nCadena sin espacios al inicio y al final: '{cadena_sin_espacios}'")