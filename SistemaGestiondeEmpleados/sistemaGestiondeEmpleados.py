
class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base
 
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self.bono = bono
        
    def calcular_salario(self):
        return super().calcular_salario() + self.bono 

