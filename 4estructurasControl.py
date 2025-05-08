# Estructuras condicionales
numero = int(input("Ingresa un número: "))

print("Estructuras condicionales:")
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número es cero.")

print("\nEstructuras de bucles:")

# Bucle for
print("Bucle for:")
for i in range(1, 6):  # Itera del 1 al 5
    print(f"Iteración {i}")

# Bucle for con lista
notificaciones = ["email", "sms", "push"]   
for medio in notificaciones:   
    if medio == "email":   
        print("Enviando correo electrónico...")   
    elif medio == "sms":   
        print("Enviando mensaje de texto...")   
    else:   
        print("Enviando notificación push...") 

# Bucle while
print("\nBucle while:")
intentos = 0   
max_intentos = 3   
while intentos < max_intentos:   
    intentos += 1   
    if intentos == 3:   
        print("Éxito en el tercer intento.")   
        break   
    print("Fallo. Reintentando...")  

# Combinación de condicionales y bucles
print("\nCombinación de condicionales y bucles:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")