import random

# 1. Generar números aleatorios básicos
print("=== Generación de números aleatorios ===")
# Número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# Número aleatorio flotante entre 0 y 1
numero_flotante = random.random()
print(f"Número aleatorio flotante entre 0 y 1: {numero_flotante}")

# Número aleatorio flotante en un rango específico
numero_flotante_rango = random.uniform(5.5, 10.5)
print(f"Número aleatorio flotante entre 5.5 y 10.5: {numero_flotante_rango}")

# Seleccionar un elemento aleatorio de una lista
colores = ["rojo", "azul", "verde", "amarillo"]
color_aleatorio = random.choice(colores)
print(f"Color aleatorio seleccionado: {color_aleatorio}")

# Mezclar una lista aleatoriamente
random.shuffle(colores)
print(f"Lista de colores mezclada: {colores}")

# 2. Simulación de experimentos
print("\n=== Simulación de experimentos ===")

# Lanzamiento de una moneda
moneda = random.choice(["Cara", "Cruz"])
print(f"Lanzamiento de una moneda: {moneda}")

# Lanzamiento de un dado
dado = random.randint(1, 6)
print(f"Lanzamiento de un dado: {dado}")

# Simulación de 10 lanzamientos de un dado
lanzamientos = [random.randint(1, 6) for _ in range(10)]
print(f"Resultados de 10 lanzamientos de un dado: {lanzamientos}")

# Simulación de una ruleta (números del 0 al 36)
ruleta = random.randint(0, 36)
print(f"Resultado de la ruleta: {ruleta}")

# 3. Tomar decisiones basadas en números aleatorios
print("\n=== Tomar decisiones ===")

# Decisión aleatoria entre dos opciones
opcion = random.choice(["Ir al cine", "Quedarse en casa"])
print(f"Decisión aleatoria: {opcion}")

# Simulación de un juego simple: adivinar un número
print("\n=== Juego: Adivina el número ===")
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina un número entre 1 y 10: "))
if intento == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"Lo siento, el número era {numero_secreto}.")