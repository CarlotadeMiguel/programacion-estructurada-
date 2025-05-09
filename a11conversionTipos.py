# Ejemplos de conversiones de tipos en Python

# 1. Conversión de un número decimal a entero
decimal = float(input("Introduce número decimal que quieras que sea entero: "))
entero = int(decimal)  # Convierte a entero (trunca la parte decimal)
print(f"Decimal: {decimal} -> Entero: {entero}")

# 2. Conversión de un número entero a cadena
entero = int(input("Introduce número entero que quieras como cadena: "))
cadena = str(entero)  # Convierte a cadena
print(f"Entero: {entero} -> Cadena: '{cadena}'")

# 3. Conversión de una cadena a número entero
cadena = "123"
entero = int(cadena)  # Convierte a entero
print(f"Cadena: '{cadena}' -> Entero: {entero}")

# 4. Conversión de una cadena a número decimal
cadena = "45.67"
decimal = float(cadena)  # Convierte a decimal
print(f"Cadena: '{cadena}' -> Decimal: {decimal}")

# 5. Conversión de un número a booleano
numero = float(input("Introduce número que quieras como booleano: "))
booleano = bool(numero)  # Convierte a booleano (0 es False, cualquier otro número es True)
print(f"Número: {numero} -> Booleano: {booleano}")

# 6. Conversión de un booleano a entero
booleano = True
entero = int(booleano)  # True se convierte a 1, False a 0
print(f"Booleano: {booleano} -> Entero: {entero}")

booleano = False
entero = int(booleano)
print(f"Booleano: {booleano} -> Entero: {entero}")

# 7. Conversión de una lista a una cadena
lista = [1, 2, 3]
cadena = str(lista)  # Convierte la lista a una representación en cadena
print(f"Lista: {lista} -> Cadena: '{cadena}'")

# 8. Conversión de una cadena a una lista
cadena = "abc"
lista = list(cadena)  # Convierte la cadena a una lista de caracteres
print(f"Cadena: '{cadena}' -> Lista: {lista}")