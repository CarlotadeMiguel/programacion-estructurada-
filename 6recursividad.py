import pickle
import os
import sys

# Cargar memo desde un archivo si existe
def cargar_memo():
    if os.path.exists("memo.pkl"):
        with open("memo.pkl", "rb") as file:
            return pickle.load(file)
    return {}

# Guardar memo en un archivo
def guardar_memo(memo):
    with open("memo.pkl", "wb") as file:
        pickle.dump(memo, file)

def factorial(n, memo):
    """Calcula el factorial de un número de forma recursiva con memoización."""
    if n in memo:  # Verifica si el resultado ya está calculado
        return memo[n]
    if n == 0 or n == 1:  # Caso base
        memo[n] = 1
    else:
        memo[n] = n * factorial(n - 1, memo)  # Almacena el resultado en memo
    return memo[n]

# Cargar el diccionario memo
memo = cargar_memo()

# Solicitar al usuario un número
try:
    numero = int(input("Ingresa un número para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        if numero > 1000:  # Advertencia para números grandes
            print("Advertencia: El cálculo del factorial puede ser muy lento para números grandes.")
            sys.setrecursionlimit(2000)  # Aumentar el límite de recursión

        try:
            resultado = factorial(numero, memo)
            print(f"El factorial de {numero} es: {resultado}")
            guardar_memo(memo)  # Guardar memo actualizado
        except RecursionError:
            print("Error: El número es demasiado grande y excede el límite de recursión.")
        except MemoryError:
            print("Error: No hay suficiente memoria para calcular el factorial de este número.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")