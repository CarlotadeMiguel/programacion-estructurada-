from enum import Enum

#Usa Enum si los valores son constantes y no cambiarán.

# Definición de un enumerado para los días de la semana
class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Uso del enumerado
def mostrar_dia(dia):
    if isinstance(dia, DiasSemana):
        print(f"El día seleccionado es: {dia.name} (valor: {dia.value})")
    else:
        print("El valor no corresponde a un día de la semana.")

# Ejemplo de uso
print("Días de la semana:")
for dia in DiasSemana:
    print(f"{dia.name} -> {dia.value}")

# Solicitar al usuario un día de la semana
try:
    valor = int(input("\nIntroduce un número (1-7) para seleccionar un día de la semana: "))
    dia_seleccionado = DiasSemana(valor)
    mostrar_dia(dia_seleccionado)
except ValueError:
    print("Error: El número introducido no corresponde a un día válido.")
except Exception as e:
    print(f"Error inesperado: {e}")