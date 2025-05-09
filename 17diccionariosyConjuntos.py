# Programa que utiliza diccionarios y conjuntos en Python

# Los diccionarios almacenan pares clave-valor.
# Acceso rápido a los valores mediante claves.
# Útil para datos estructurados.

# Los conjuntos almacenan elementos únicos y no ordenados.
# Eliminación automática de duplicados.
# Operaciones matemáticas rápidas (unión, intersección, etc.).

# === Diccionarios ===
print("=== Diccionarios ===")

# Crear un diccionario para almacenar información de estudiantes
estudiantes = {
    "Juan": 20,
    "María": 22,
    "Pedro": 19,
    "Ana": 21
}

# Acceso a elementos
print("\nEdad de Juan:", estudiantes["Juan"])

# Añadir un nuevo elemento
estudiantes["Luis"] = 23
print("Diccionario después de añadir a Luis:", estudiantes)

# Modificar un elemento
estudiantes["María"] = 23
print("Diccionario después de modificar la edad de María:", estudiantes)

# Eliminar un elemento
del estudiantes["Pedro"]
print("Diccionario después de eliminar a Pedro:", estudiantes)

# Usar get() para obtener un valor con un valor predeterminado
print("\nEdad de Juan:", estudiantes.get("Juan", "No encontrado"))
print("Edad de Carlos:", estudiantes.get("Carlos", "No encontrado"))

# Usar pop() para eliminar y obtener un valor
edad_ana = estudiantes.pop("Ana")
print("Edad de Ana eliminada:", edad_ana)
print("Diccionario después de pop:", estudiantes)

# Usar popitem() para eliminar el último par clave-valor
ultimo = estudiantes.popitem()
print("Último elemento eliminado:", ultimo)
print("Diccionario después de popitem:", estudiantes)

# Actualizar el diccionario con update()
estudiantes.update({"Carlos": 24, "Ana": 22})
print("Diccionario actualizado:", estudiantes)

# Recorrer el diccionario
print("\nRecorrido del diccionario:")
for nombre, edad in estudiantes.items():
    print(f"{nombre}: {edad} años")

# Verificar si una clave existe
if "Ana" in estudiantes:
    print("\nAna está en el diccionario.")

# Obtener todas las claves y valores
print("Claves:", estudiantes.keys())
print("Valores:", estudiantes.values())

# Crear un nuevo diccionario con fromkeys()
nuevo_diccionario = dict.fromkeys(["clave1", "clave2", "clave3"], 0)
print("\nNuevo diccionario creado con fromkeys:", nuevo_diccionario)

# Crear una copia del diccionario
copia_estudiantes = estudiantes.copy()
print("Copia del diccionario:", copia_estudiantes)

# Limpiar el diccionario con clear()
estudiantes.clear()
print("Diccionario vacío:", estudiantes)

# === Conjuntos ===
print("\n=== Conjuntos ===")

# Crear un conjunto para almacenar materias
materias = {"Matemáticas", "Física", "Química", "Historia"}

# Añadir un elemento
materias.add("Biología")
print("Conjunto después de añadir Biología:", materias)

# Eliminar un elemento
materias.remove("Historia")
print("Conjunto después de eliminar Historia:", materias)

# Usar discard() para eliminar sin error
materias.discard("Historia")  # No genera error si no existe
print("Conjunto después de descartar Historia:", materias)

# Operaciones con conjuntos
otro_conjunto = {"Física", "Química", "Inglés"}

# Unión
union = materias.union(otro_conjunto)
print("\nUnión de conjuntos:", union)

# Intersección
interseccion = materias.intersection(otro_conjunto)
print("Intersección de conjuntos:", interseccion)

# Diferencia
diferencia = materias.difference(otro_conjunto)
print("Diferencia de conjuntos:", diferencia)

# Diferencia simétrica
simetrica = materias.symmetric_difference(otro_conjunto)
print("Diferencia simétrica:", simetrica)

# Verificar si un conjunto es un subconjunto
es_subconjunto = {"Física", "Química"}.issubset(materias)
print("\n¿Es {'Física', 'Química'} un subconjunto?:", es_subconjunto)

# Verificar si un conjunto es un superconjunto
es_superconjunto = materias.issuperset({"Física"})
print("¿Es superconjunto?:", es_superconjunto)

# Verificar si dos conjuntos son disjuntos
disjuntos = materias.isdisjoint({"Inglés", "Arte"})
print("¿Son disjuntos?:", disjuntos)

# Verificar si un elemento está en el conjunto
if "Matemáticas" in materias:
    print("\nMatemáticas está en el conjunto de materias.")

# Recorrer un conjunto
print("\nRecorrido del conjunto:")
for materia in materias:
    print(materia)

# Crear una copia del conjunto
copia_materias = materias.copy()
print("\nCopia del conjunto:", copia_materias)

# Limpiar el conjunto con clear()
materias.clear()
print("Conjunto vacío:", materias)