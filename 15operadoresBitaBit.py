#Los operadores bit a bit (bitwise operators) en Python son operadores que trabajan directamente con los bits de los números. Estos operadores realizan operaciones a nivel binario, manipulando los bits individuales de los operandos. Son útiles en programación de bajo nivel, como en sistemas embebidos, criptografía, manipulación de máscaras de bits, y optimización de ciertas operaciones matemáticas.

# Programa que utiliza operadores bit a bit

# Definir dos números
a = 5  # En binario: 0b0101 el prefijo 0b se utiliza para indicar que un número está representado en notación binaria.
b = 3  # En binario: 0b0011

print(f"Números iniciales: a = {a} (binario: {bin(a)}), b = {b} (binario: {bin(b)})\n")

# 1. AND bit a bit (&)
# Compara los bits de dos números y devuelve 1 si ambos bits son 1.
# En este caso, el resultado será 1 (0b0001) porque solo el último bit coincide.
resultado_and = a & b
print(f"AND bit a bit: {a} & {b} = {resultado_and} (binario: {bin(resultado_and)})")

# 2. OR bit a bit (|)
# Compara los bits de dos números y devuelve 1 si al menos uno de los bits es 1.
resultado_or = a | b
print(f"OR bit a bit: {a} | {b} = {resultado_or} (binario: {bin(resultado_or)})")

# 3. XOR bit a bit (^)
# Compara los bits de dos números y devuelve 1 si los bits son diferentes.
# En este caso, el resultado será 6 (0b0110) porque los bits son diferentes.
# 0b0101 ^ 0b0011 = 0b0110
resultado_xor = a ^ b
print(f"XOR bit a bit: {a} ^ {b} = {resultado_xor} (binario: {bin(resultado_xor)})")

# 4. NOT bit a bit (~)
# Invierte todos los bits del número.
# Esto significa que convierte los bits de 1 a 0 y los bits de 0 a 1
# En este caso, el resultado será -6 (0b1010).
# En Python, los números negativos se representan en complemento a dos.

# Representación binaria de 5:
# 5 en binario es 0b0101 (en 8 bits: 00000101).

# Inversión de bits con ~:
# Invierte todos los bits: 11111010.

# Interpretación como número negativo:
# El resultado 11111010 es el complemento a dos de -6:
# Invierte los bits de 11111010: 00000101.
# Suma 1: 00000110 → 6.
# Por lo tanto, 11111010 representa -6.

# Resultado:
# ~5 = -6.

#Formula general ~a = -(a + 1)

resultado_not_a = ~a
print(f"NOT bit a bit: ~{a} = {resultado_not_a} (binario: {bin(resultado_not_a)})")

# 5. Desplazamiento a la izquierda (<<)
# Desplaza los bits a la izquierda, multiplicando el número por 2 por cada desplazamiento.
# En este caso, el resultado será 10 (0b1010)
# 0b0101 << 1 = 0b1010
desplazamiento_izquierda = a << 1   
print(f"Desplazamiento a la izquierda: {a} << 1 = {desplazamiento_izquierda} (binario: {bin(desplazamiento_izquierda)})")

# 6. Desplazamiento a la derecha (>>)
# Desplaza los bits a la derecha, dividiendo el número por 2 por cada desplazamiento.
# En este caso, el resultado será 2 (0b0010)
desplazamiento_derecha = a >> 1
print(f"Desplazamiento a la derecha: {a} >> 1 = {desplazamiento_derecha} (binario: {bin(desplazamiento_derecha)})")

# 7. Máscara de bits: Activar un bit específico
# Se utiliza una máscara para activar un bit específico en un número.
# En este caso, activamos el tercer bit (0b0100).
# 0b0101 | 0b0010 = 0b0111
mascara = 0b0010  # Máscara para activar el tercer bit
resultado_mascara = a | mascara
print(f"\nAplicar máscara para activar el tercer bit: {a} | {mascara} = {resultado_mascara} (binario: {bin(resultado_mascara)})")

# 8. Máscara de bits: Desactivar un bit específico
mascara = 0b0001  # Máscara para desactivar el segundo bit
# 0b0101 & 0b1110 = 0b0100
resultado_mascara = a & mascara
print(f"Aplicar máscara para desactivar el segundo bit: {a} & {mascara} = {resultado_mascara} (binario: {bin(resultado_mascara)})")

# 9. Verificar si un bit está activado
bit_a_verificar = 0b0100  # Verificar el tercer bit
bit_activado = a & bit_a_verificar
print(f"\nVerificar si el tercer bit está activado en {a}: {'Sí' if bit_activado else 'No'}")