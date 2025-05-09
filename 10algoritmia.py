
# Plan:
# Solicitar al usuario que introduzca tres números.
# Comparar los números usando estructuras condicionales (if-elif-else).
# Determinar cuál es el mayor de los tres números.
# Mostrar el resultado.

# Algoritmo para encontrar el máximo de tres números

# Solicitar al usuario que introduzca tres números
print("Introduce tres números para encontrar el máximo:")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Comparar los números para encontrar el máximo
if num1 >= num2 and num1 >= num3:
    maximo = num1
elif num2 >= num1 and num2 >= num3:
    maximo = num2
else:
    maximo = num3

# Mostrar el resultado
print(f"El número máximo es: {maximo}")