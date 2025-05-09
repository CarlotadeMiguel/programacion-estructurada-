# Manejo de excepciones en Python

# Ejemplo 1: Manejo de excepciones al convertir una cadena a número
try:
    cadena = input("Introduce un número decimal: ")
    numero = float(cadena)  # Intentar convertir la cadena a número decimal
    print(f"El número convertido es: {numero}")
except ValueError:
    print("Error: No se pudo convertir la cadena a un número decimal.")
finally:
    print("Finalizó el intento de conversión.\n")

# Ejemplo 2: División entre cero
try:
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    resultado = numerador / denominador  # Intentar realizar la división
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes introducir números enteros.")
finally:
    print("Finalizó el intento de división.\n")

# Ejemplo 3: Lanzamiento manual de una excepción
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")  # Lanzar una excepción
    print(f"Tu edad es: {edad}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Finalizó la validación de la edad.\n")

# Ejemplo 4: Acceso a un índice fuera de rango en una lista
try:
    lista = [1, 2, 3]
    indice = int(input("Introduce un índice para la lista [0-2]: "))
    print(f"El valor en el índice {indice} es: {lista[indice]}")
except IndexError:
    print("Error: El índice está fuera del rango permitido.")
except ValueError:
    print("Error: Debes introducir un número entero.")
finally:
    print("Finalizó el intento de acceso a la lista.\n")