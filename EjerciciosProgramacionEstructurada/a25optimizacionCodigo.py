from functools import lru_cache

# === Ejemplo 1: Optimización con Memoización ===
@lru_cache(maxsize=None)
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci utilizando memoización."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# === Ejemplo 2: Eliminación de Bucles Innecesarios ===
def suma_pares(lista):
    """Suma solo los números pares de una lista de manera eficiente."""
    return sum(x for x in lista if x % 2 == 0)

# === Ejemplo 3: Uso Eficiente de Estructuras de Datos ===
def contar_ocurrencias(lista):
    """Cuenta las ocurrencias de cada elemento utilizando un diccionario."""
    from collections import Counter
    return Counter(lista)

# === Programa Principal ===
if __name__ == "__main__":
    print("=== Ejemplo 1: Optimización con Memoización ===")
    n = 35
    print(f"El {n}-ésimo número de Fibonacci es: {fibonacci(n)}")

    print("\n=== Ejemplo 2: Eliminación de Bucles Innecesarios ===")
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista original: {lista}")
    print(f"Suma de números pares: {suma_pares(lista)}")

    print("\n=== Ejemplo 3: Uso Eficiente de Estructuras de Datos ===")
    lista_repetida = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(f"Lista original: {lista_repetida}")
    print(f"Conteo de ocurrencias: {contar_ocurrencias(lista_repetida)}")