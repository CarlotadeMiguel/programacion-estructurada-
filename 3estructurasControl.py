# Operadores aritméticos
a = 10
b = 3

print("Operadores aritméticos:")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")
print()

# Operadores lógicos
x = True
y = False

print("Operadores lógicos:")
print(f"AND: {x} and {y} = {x and y}")
print(f"OR: {x} or {y} = {x or y}")
print(f"NOT: not {x} = {not x}")
print()

# Combinación de operadores aritméticos y lógicos
print("Combinación de operadores:")
resultado = (a + b > 10) and (a - b < 10)
print(f"({a} + {b} > 10) and ({a} - {b} < 10) = {resultado}")