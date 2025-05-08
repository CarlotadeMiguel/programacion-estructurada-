#Separador
filas = ("*" * 10 + "\n") * 2

# Ejemplo de tipos de datos primitivos y estructurados en Python

# 1. Enteros (int)
entero = 42  # Dominio: números enteros (-∞, ∞)
print(f"Entero: {entero}, Tipo: {type(entero)}, Operadores: +, -, *, /, %, //, **")
print(filas)

# 2. Reales (float)
real = 3.14  # Dominio: números reales (limitado por la precisión de la máquina)
print(f"Real: {real}, Tipo: {type(real)}, Operadores: +, -, *, /, %, //, **")
print(filas)

# 3. Caracteres (str)
caracter = 'A'  # Dominio: cualquier carácter Unicode
print(f"Caracter: {caracter}, Tipo: {type(caracter)}, Operadores: + (concatenar), * (repetir)")
repetido = caracter * 3  # Repite el string 3 veces
print(f"Texto original: {caracter}, Texto repetido: {repetido}")
print(filas)

# 4. Arrays (listas en Python)
array = [1, 2, 3, 4, 5]  # Dominio: colección ordenada de elementos
print(f"Array: {array}, Tipo: {type(array)}, Operadores: + (concatenar), * (repetir), [] (indexar)")
print(array + [6])
print(filas)

# 5. Estructuras (diccionarios en Python)
estructura = {"nombre": "Juan", "edad": 30}  # Dominio: pares clave-valor
print(f"Estructura: {estructura}, Tipo: {type(estructura)}, Operadores: [] (acceso), in (verificar clave)")
print(filas)

# 6. Enumerados (usando enum)
from enum import Enum

class Colores(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

color = Colores.ROJO
print(f"Enumerado: {color}, Tipo: {type(color)}, Valores: {[c.name for c in Colores]}")
print(Colores.ROJO.value)
print(Colores(1).value)
print(Colores(1).name)
print(filas)
