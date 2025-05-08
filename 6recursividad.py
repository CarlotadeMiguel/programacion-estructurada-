def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:  # Caso base: el factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Solicitar al usuario un número
numero = int(input("Ingresa un número para calcular su factorial: "))

# Validar que el número sea no negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")