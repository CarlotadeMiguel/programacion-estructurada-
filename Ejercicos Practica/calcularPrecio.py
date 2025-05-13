def calcular_total( 
    precios: list[float],          # Lista de precios (obligatorio) 
    descuento: float = 0.0         # Parámetro opcional (valor por defecto) 
) -> float:                        # Retorna un número decimal 
    subtotal = sum(precios)        # Suma todos los precios 
    return subtotal - (subtotal * descuento)  # Aplica descuento 
# Uso simple:   
print(calcular_total([10, 20]))              # 30.0 (sin descuento)   
print(calcular_total([10, 20], descuento=0.1))  # 27.0 (10% off)