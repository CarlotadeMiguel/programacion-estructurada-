# Variable global
mensaje_global = "Soy una variable global"

def funcion_ambito():
    # Variable local
    mensaje_local = "Soy una variable local"
    print(mensaje_local)  # Acceso a la variable local
    print(mensaje_global)  # Acceso a la variable global desde dentro de la función

def modificar_global():
    global mensaje_global  # Declarar que se usará la variable global
    mensaje_global = "He sido modificada desde una función"
    print("Variable global modificada dentro de la función")

# Llamadas y demostración
print("Antes de llamar a la función:")
print(mensaje_global)  # Acceso a la variable global

print("\nDentro de la función:")
funcion_ambito()

print("\nModificando la variable global:")
modificar_global()
print(mensaje_global)  # Ver el cambio en la variable global

# Intentar acceder a una variable local fuera de su función
try:
    print(mensaje_local)  # Esto generará un error porque mensaje_local es local
except NameError as e:
    print(f"\nError: {e}")