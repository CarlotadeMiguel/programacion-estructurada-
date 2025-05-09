import pickle
import os
import sys
from functools import lru_cache

# Cargar memo desde un archivo si existe
def cargar_memo():
    if os.path.exists("memo.pkl"):
        try:
            with open("memo.pkl", "rb") as file:
                memo = pickle.load(file)
                if not isinstance(memo, dict):  # Verificar que sea un diccionario
                    raise ValueError("El archivo memo.pkl no contiene un diccionario válido.")
                return memo
        except (pickle.UnpicklingError, ValueError, EOFError):
            print("Advertencia: El archivo memo.pkl está corrupto. Se reiniciará el memo.")
            os.remove("memo.pkl")  # Eliminar el archivo corrupto
    return {}

# Guardar memo en un archivo
def guardar_memo(memo):
    with open("memo.pkl", "wb") as file:
        pickle.dump(memo, file)

# Función factorial con lru_cache
@lru_cache(maxsize=None)
def factorial_lru(n):
    """Calcula el factorial de un número de forma recursiva con lru_cache."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_lru(n - 1)

# Función para combinar lru_cache con persistencia
def factorial(n, memo):
    """Calcula el factorial utilizando lru_cache y actualiza el memo persistente."""
    if n in memo:  # Si ya está en el memo persistente
        return memo[n]
    resultado = factorial_lru(n)  # Calcular usando lru_cache
    memo[n] = resultado  # Actualizar el memo persistente
    return resultado

# Programa principal con manejo mejorado de excepciones
try:
    # Cargar el diccionario memo
    memo = cargar_memo()
    
    # Solicitar al usuario un número
    numero = int(input("Ingresa un número para calcular su factorial: "))
    
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        # Verificación explícita para números grandes
        if numero > 1000:
            print("Advertencia: El cálculo del factorial puede ser muy lento para números grandes.")
            
            # Configurar el límite de recursión
            limite_anterior = sys.getrecursionlimit()
            try:
                sys.setrecursionlimit(2000)
                
                # Verificar si el número excede incluso el nuevo límite
                if numero > 1800:  # Dejamos margen de seguridad
                    raise RecursionError("El número es demasiado grande")
                
                try:
                    resultado = factorial(numero, memo)
                    print(f"El factorial de {numero} es: {resultado}")
                    guardar_memo(memo)  # Guardar memo actualizado
                except (RecursionError, OverflowError):
                    print("Error: El número es demasiado grande y excede el límite de recursión.")
            finally:
                # Restaurar el límite original de recursión
                sys.setrecursionlimit(limite_anterior)
        else:
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
# Capturar RecursionError incluso fuera del bloque try interno
except RecursionError:
    print("Error: El número es demasiado grande y excede el límite de recursión.")