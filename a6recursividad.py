import pickle
import os
import sys

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

def factorial(n, memo):
    """Calcula el factorial de un número de forma recursiva con memoización."""
    # Verificar primero si el número es demasiado grande antes de cualquier cálculo
    if n > sys.getrecursionlimit() - 100:  # Margen de seguridad
        raise RecursionError("Se excedió el límite de recursión")
        
    if n in memo:  # Verifica si el resultado ya está calculado
        return memo[n]
    if n == 0 or n == 1:  # Caso base
        memo[n] = 1
    else:
        memo[n] = n * factorial(n - 1, memo)  # Almacena el resultado en memo
    return memo[n]

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
                    # Usamos un diccionario temporal para evitar problemas con memo existente
                    memo_temp = {}
                    resultado = factorial(numero, memo_temp)
                    print(f"El factorial de {numero} es: {resultado}")
                    # Solo actualizamos memo si el cálculo fue exitoso
                    memo.update(memo_temp)
                    guardar_memo(memo)
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
