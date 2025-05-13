def sumar (a , b):
    return a + b
def restar (a , b):
    return a - b
def multiplicar (a , b):
    return a * b
def dividir (a , b):
    if b == 0:
        return "No se puede dividir entre cero" 
    else:
        return a / b    


def main():
    while True:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        print("¿Qué operación desea realizar? (+ para suma, - para resta, * para multiplicación, / para división):")
        operacion = input()

        if operacion == "+":
            resultado = sumar(num1, num2)
            print(f"La suma de {num1} y {num2} es: {resultado}")
        elif operacion == "-":
            resultado = restar(num1, num2)
            print(f"La resta de {num1} y {num2} es: {resultado}")
        elif operacion == "*":
            resultado = multiplicar(num1, num2)
            print(f"La multiplicación de {num1} y {num2} es: {resultado}")
        elif operacion == "/":
            resultado = dividir(num1, num2)
            print(f"La división de {num1} y {num2} es: {resultado}")
        else:
            print("Operación no válida")

        # Preguntar si el usuario desea realizar otra operación
        print("\n¿Desea realizar otra operación? (s/n):")
        continuar = input().lower()
        if continuar != "s":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

# Llamar a la función principal
if __name__ == "__main__":
    main()