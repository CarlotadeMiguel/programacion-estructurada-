import random

print("=== Bienvenido al programa de números aleatorios ===")

# 1. Generación de números aleatorios básicos
print("\n=== Generación de números aleatorios ===")
rango_inferior = int(input("Introduce el límite inferior para un número aleatorio: "))
rango_superior = int(input("Introduce el límite superior para un número aleatorio: "))
numero_aleatorio = random.randint(rango_inferior, rango_superior)
print(f"Número aleatorio entre {rango_inferior} y {rango_superior}: {numero_aleatorio}")

# Número flotante aleatorio
print("\nGenerando un número flotante aleatorio entre 0 y 1...")
numero_flotante = random.random()
print(f"Número flotante aleatorio: {numero_flotante:.2f}")

# Seleccionar un elemento aleatorio de una lista proporcionada por el usuario
print("\n=== Selección aleatoria de una lista ===")
elementos = [elemento.strip() for elemento in input("Introduce elementos separados por comas: ").split(",")]
elemento_aleatorio = random.choice(elementos)
print(f"Elemento aleatorio seleccionado: {elemento_aleatorio.strip()}")

# Mezclar una lista proporcionada por el usuario
print("\nMezclando los elementos de tu lista...")
random.shuffle(elementos)
print(f"Lista mezclada: {elementos}")

# 2. Simulación de experimentos
print("\n=== Simulación de experimentos ===")

# Lanzamiento de una moneda
print("\nLanzamiento de una moneda...")
moneda = random.choice(["Cara", "Cruz"])
print(f"Resultado: {moneda}")

# Lanzamiento de un dado
print("\nLanzamiento de un dado...")
dado = random.randint(1, 6)
print(f"Resultado del dado: {dado}")

# Simulación de varios lanzamientos de un dado
print("\nSimulación de lanzamientos de un dado...")
cantidad_lanzamientos = int(input("¿Cuántas veces quieres lanzar el dado? "))
lanzamientos = [random.randint(1, 6) for _ in range(cantidad_lanzamientos)]
print(f"Resultados de los lanzamientos: {lanzamientos}")

# Simulación de una ruleta
print("\nSimulación de una ruleta...")
ruleta = random.randint(0, 36)
print(f"Resultado de la ruleta: {ruleta}")

# 3. Juego interactivo: Adivina el número
print("\n=== Juego: Adivina el número ===")
numero_secreto = random.randint(1, 10)
intentos = 0
while True:
    intento = int(input("Adivina un número entre 1 y 10: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

# 4. Decisión aleatoria
print("\n=== Decisión aleatoria ===")
opciones = [elemento.strip() for elemento in input("Introduce opciones separadas por comas para tomar una decisión aleatoria:").split(",")]
decision = random.choice(opciones)
print(f"Decisión tomada: {decision.strip()}")

print("\n=== Gracias por usar el programa de números aleatorios ===")