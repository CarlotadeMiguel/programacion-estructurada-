
#Es una buena práctica usar @property cuando quieres proteger los datos
# o necesitas lógica especial al acceder o modificar atributos.

class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self._nombre = nombre
        self._edad = None
        self.edad = edad   
        self._salario_base = salario_base
 
    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
 
    @property
    def edad(self):
        return self._edad
 
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print ("La edad no puede ser negativa")
            exit()
        self._edad = nueva_edad
 
    @property
    def salario_base(self):
        return self._salario_base
 
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        self._salario_base = nuevo_salario
 
    def calcular_salario(self):
        return self._salario_base
 
 
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self._bono = bono
 
    @property
    def bono(self):
        return self._bono
 
    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono
 
    def calcular_salario(self):
        return super().calcular_salario() + self._bono

def calcular_y_mostrar_salario(empleado):
    print(f"El salario de {empleado.nombre} es: {empleado.calcular_salario()}")
 
 
# Prueba del sistema
empleado1 = Empleado("Juan", 30, 50000)
gerente1 = Gerente("Ana", 35, 60000, 10000)
 
print(empleado1.calcular_salario())  # Salida esperada: 50000
print(gerente1.calcular_salario())   # Salida esperada: 70000
 
calcular_y_mostrar_salario(empleado1)  # Salida esperada: El salario de Juan es: 50000
calcular_y_mostrar_salario(gerente1)   # Salida esperada: El salario de Ana es: 70000

empleado2 = Empleado("Juan", -30, 50000) #Salida esperada: La edad no puede ser negativa y parara el programa
