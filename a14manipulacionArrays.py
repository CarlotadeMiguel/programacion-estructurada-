# Importar el módulo array para trabajar con arrays
from array import array

# Listas: Pueden contener elementos de diferentes tipos en la misma lista.
# Son más generales y compatibles con la mayoría de las librerías de Python.
# Ejemplo: Puedes pasar listas a funciones de librerías como pandas o matplotlib.

# Arrays: Solo pueden contener elementos de un único tipo.
# Son más eficientes en términos de memoria y rendimiento para operaciones numéricas.
# Tienen menos métodos que las listas

# 1. Creación de un array
# Crear un array de enteros
numeros = array('i', [10, 20, 30, 40, 50])
print("Array inicial:", numeros)

# 2. Acceso a elementos
print("\nAcceso a elementos:")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")

# 3. Modificación de elementos
print("\nModificación de elementos:")
numeros[1] = 25  # Cambiar el segundo elemento
print("Array después de modificar el segundo elemento:", numeros)

# 4. Recorrido del array
print("\nRecorrido del array:")
for numero in numeros:
    print(numero, end=" ")
print()

# 5. Añadir elementos al array
print("\nAñadir elementos al array:")
numeros.append(60)  # Añadir un elemento al final
print("Array después de añadir un elemento:", numeros)

# 6. Eliminar elementos del array
print("\nEliminar elementos del array:")
numeros.remove(30)  # Eliminar el primer elemento con valor 30
print("Array después de eliminar el elemento con valor 30:", numeros)

# Eliminar un elemento por índice
print("\nEliminar un elemento por índice:")
indice = 2
elemento_eliminado = numeros.pop(indice)
print(f"Elemento eliminado en el índice {indice}: {elemento_eliminado}")
print("Array después de eliminar el elemento:", numeros)

# 7. Longitud del array
print("\nLongitud del array:")
print(f"El array tiene {len(numeros)} elementos.")

# 8. Búsqueda de un elemento
print("\nBúsqueda de un elemento:")
valor = 40
if valor in numeros:
    print(f"El valor {valor} está en el array en el índice {numeros.index(valor)}.")
else:
    print(f"El valor {valor} no está en el array.")

# 9. Insertar un elemento en una posición específica
print("\nInsertar un elemento en una posición específica:")
numeros.insert(2, 35)  # Insertar el valor 35 en la posición 2
print("Array después de la inserción:", numeros)

# 10. Revertir el array
print("\nRevertir el array:")
numeros.reverse()
print("Array después de revertir:", numeros)

# 11. Copiar el array
print("\nCopiar el array:")
copia_numeros = numeros[:]
print("Copia del array:", copia_numeros)

# 12. Extender el array con otro array
print("\nExtender el array:")
otros_numeros = array('i', [70, 80, 90])
numeros.extend(otros_numeros)
print("Array después de extender:", numeros)

# 13. Contar ocurrencias de un elemento
print("\nContar ocurrencias de un elemento:")
ocurrencias = numeros.count(60)
print(f"El número 60 aparece {ocurrencias} veces en el array.")

# 14. Convertir el array a una lista
print("\nConvertir el array a una lista:")
lista_numeros = list(numeros)
print("Lista convertida:", lista_numeros)

# 15 Ordenar el array
print("\nOrdenar el array:")
numeros = array('i', sorted(numeros))  # Usar sorted() para arrays
print("Array ordenado:", numeros)

# 16 Recorrer el array con índices
print("\nRecorrer el array con índices:")
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")

# 16 Sumar todos los elementos
print("\nSumar todos los elementos del array:")
suma = sum(numeros)
print(f"La suma de los elementos es: {suma}")

# 17 Multiplicar todos los elementos
print("\nMultiplicar todos los elementos del array:")
producto = 1
for num in numeros:
    producto *= num
print(f"El producto de los elementos es: {producto}")

# 18 Obtener el valor máximo y mínimo
print("\nObtener el valor máximo y mínimo:")
maximo = max(numeros)
minimo = min(numeros)
print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")

# 19 Obtener el promedio
print("\nObtener el promedio:")
promedio = suma / len(numeros)
print(f"El promedio es: {promedio}")

# 20 Vaciar el array
print("\nVaciar el array:")
numeros.clear()
print("Array después de vaciar:", numeros)
