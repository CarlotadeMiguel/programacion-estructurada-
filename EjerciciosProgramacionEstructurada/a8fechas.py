from datetime import datetime, timedelta

# Programa para manejar fechas

# 1. Obtener la fecha y hora actual
fecha_actual = datetime.now()
print(f"Fecha y hora actual: {fecha_actual}")

# 2. Formatear la fecha
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {fecha_formateada}")

# 3. Crear una fecha específica
fecha_especifica = datetime(2023, 12, 25, 10, 30, 0)
print(f"Fecha específica: {fecha_especifica}")

# 4. Calcular la diferencia entre dos fechas
fecha_futura = datetime(2025, 9, 8)
diferencia = fecha_futura - fecha_actual
 # Restar dos objetos datetime devuelve un objeto timedelta, que contiene la diferencia en días, segundos, etc.
print(type(diferencia))
print(f"Días hasta el {fecha_futura.strftime('%d/%m/%Y')}: {diferencia.days} días")

# 5. Sumar o restar días a una fecha
dias_a_sumar = 10
nueva_fecha = fecha_actual + timedelta(days=dias_a_sumar)
print(f"Fecha después de sumar {dias_a_sumar} días: {nueva_fecha.strftime('%d/%m/%Y')}")

dias_a_restar = 15
fecha_resta = fecha_actual - timedelta(days=dias_a_restar)
print(f"Fecha después de restar {dias_a_restar} días: {fecha_resta.strftime('%d/%m/%Y')}")

# 6. Comparar fechas
if fecha_actual < fecha_futura:
    print("La fecha actual es anterior a la fecha futura.")
else:
    print("La fecha actual es posterior o igual a la fecha futura.")