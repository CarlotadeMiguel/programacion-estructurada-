# Programa que trabaja con listas y tuplas en Python

# 1. Creación de una lista y una tupla
mi_lista = [40, 10, 30, 20, 50]  # Lista: mutable
mi_tupla = (10, 20, 30, 40, 50)  # Tupla: inmutable

print("Lista inicial:", mi_lista)
print("Tupla inicial:", mi_tupla)

# 2. Acceso a elementos
print("\nAcceso a elementos:")
print(f"Primer elemento de la lista: {mi_lista[0]}")
print(f"Primer elemento de la tupla: {mi_tupla[0]}")

# 3. Modificación de elementos
print("\nModificación de elementos en la lista:")
mi_lista[1] = 25  # Cambiar el segundo elemento de la lista
print("Lista después de la modificación:", mi_lista)

# Las tuplas no permiten modificación de elementos
try:
    mi_tupla[1] = 25  # Esto generará un error
except TypeError as e:
    print("Error al intentar modificar una tupla:", e)

# 4. Añadir y eliminar elementos
print("\nAñadir y eliminar elementos en la lista:")
mi_lista.append(60)  # Añadir un elemento al final de la lista
print("Lista después de añadir un elemento:", mi_lista)
mi_lista.remove(30)  # Eliminar el primer elemento con valor 30
print("Lista después de eliminar un elemento:", mi_lista)

# Las tuplas no permiten añadir ni eliminar elementos
try:
    mi_tupla.append(60)  # Esto generará un error
except AttributeError as e:
    print("Error al intentar añadir un elemento a una tupla:", e)

# 5. Recorrido de listas y tuplas
print("\nRecorrido de la lista:")
for elemento in mi_lista:
    print(elemento, end=" ")
print()

#Las tuplas son más rápidas que las listas para iterar, ya que son inmutables.
print("\nRecorrido de la tupla:")
for elemento in mi_tupla:
    print(elemento, end=" ")
print()

# 6. Conversión entre listas y tuplas
print("\nConversión entre listas y tuplas:")
nueva_tupla = tuple(mi_lista)  # Convertir lista a tupla
print("Tupla convertida desde la lista:", nueva_tupla)
nueva_lista = list(mi_tupla)  # Convertir tupla a lista
print("Lista convertida desde la tupla:", nueva_lista)

# 7. Uso de listas y tuplas en distintos contextos
print("\nUso en distintos contextos:")
# Listas: útiles para datos que cambian frecuentemente
mi_lista.append(70)
print("Lista modificada dinámicamente:", mi_lista)

mi_lista.pop()
print("Lista eliminar ultimo elemento de la lista:", mi_lista)

# Tuplas: útiles para datos constantes o inmutables
coordenadas = (10.5, 20.3)  # Ejemplo de tupla para coordenadas
print("Tupla de coordenadas (constante):", coordenadas)

# 8. Ordenar elementos
mi_lista.sort()  # Ordena la lista en su lugar
print("Lista ordenada:", mi_lista)

# Usar sorted() para obtener una nueva lista ordenada sin modificar la original
lista_ordenada = sorted(mi_lista, reverse=True)  # Orden descendente
print("Lista ordenada en orden descendente:", lista_ordenada)

# 9. Filtrar elementos
filtrada = [x for x in mi_lista if x > 30]  # Filtrar elementos mayores a 30
print("Lista filtrada:", filtrada)

# 10. Buscar elementos
if 40 in mi_lista:
    print("El número 40 está en la lista en el índice:", mi_lista.index(40))

# 11. Invertir orden 
mi_lista.reverse()  # Invierte la lista en su lugar
print("Lista invertida .reverse():", mi_lista)

# Usar reversed() para obtener una nueva lista invertida
lista_invertida = list(reversed(mi_lista))
print("Nueva lista invertida list(reversed()):", lista_invertida)

# 12. Eliminar duplicados de la lista
mi_lista = [10, 20, 30, 20, 10, 40]
sin_duplicados = list(set(mi_lista))
print("Lista sin duplicados:", sin_duplicados)

# 13 Conectar listas
#Combina dos listas y devuelve una nueva lista sin modificar las listas originales.
#Consume más memoria porque se crea una nueva lista.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print("Lista concatenada:", concatenada)

# Usar extend() para modificar la lista original
# Modifica la lista original
# Más eficiente en términos de memoria porque no crea una nueva lista.
lista1.extend(lista2)
print("Lista extendida:", lista1)

# 14 Tuplas Claves en diccionarios
diccionario = {coordenadas: "Punto A"}
print("Valor asociado a las coordenadas:", diccionario[coordenadas])

# 15. Desempaquetado de tuplas
tupla = (10, 20, 30)
a, b, c = tupla
print(f"a = {a}, b = {b}, c = {c}")

# 16. retorno multiples valores
def calcular(a, b):
    suma = a + b
    producto = a * b
    return suma, producto  # Devuelve una tupla

resultado = calcular(5, 10)
print("Suma y producto:", resultado)