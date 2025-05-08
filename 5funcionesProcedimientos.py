# Función con parámetros (retorna un valor)
def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

# Procedimiento (no retorna valor, solo realiza una tarea)
def mostrar_mensaje(mensaje):
    """Muestra un mensaje en la consola."""
    print(f"Mensaje: {mensaje}")

# Ejemplo de parámetros por valor, no se modifica el valor original crea una copia
def duplicar_valor(numero):
    """Intenta duplicar el valor de un número (por valor)."""
    numero *= 2
    print(f"Valor dentro de la función: {numero}")

def modificar_string(cadena):
    """Intenta modificar un string."""
    cadena += " modificado"
    print(f"String dentro de la función: {cadena}")

# Ejemplo de parámetros por valor, cambiar valor
def duplicar_valorN(numero):
    """Duplica el valor de un número (por valor)."""
    numero *= 2
    print(f"Valor dentro de la función N: {numero}")
    return numero

# Ejemplo de parámetros por referencia
def agregar_elemento(lista):
    """Agrega un elemento a la lista (por referencia)."""
    lista.append("Nuevo elemento")
    print(f"Lista dentro de la función: {lista}")

# Llamadas a las funciones y procedimientos
print("Funciones y procedimientos en Python:\n")

# Llamada a la función con parámetros

print("Ingrese el primer número:")
num1 = float(input())
print("Ingrese el segundo número:")
num2 = float(input())
resultado = sumar(num1, num2)
print(f"Resultado de la suma: {resultado}\n")

# Llamada al procedimiento
mostrar_mensaje("Hola, este es un procedimiento.\n")

# Parámetros por valor
numero = 10
print(f"Valor antes de la función: {numero}")
duplicar_valor(numero)
print(f"Valor después de la función: {numero}\n")

# Llamada a la función
texto = "Texto original"
print(f"String antes de la función: {texto}")
modificar_string(texto)
print(f"String después de la función: {texto}\n")

# Parametros por vqlor, cambiar valor
numeroN = 10
print(f"Valor antes de la función N: {numeroN}")
numeroN = duplicar_valorN(numeroN)
print(f"Valor después de la función N: {numeroN}\n")

# Parámetros por referencia
mi_lista = [1, 2, 3]
print(f"Lista antes de la función: {mi_lista}\n")
agregar_elemento(mi_lista)
print(f"Lista después de la función: {mi_lista}\n")