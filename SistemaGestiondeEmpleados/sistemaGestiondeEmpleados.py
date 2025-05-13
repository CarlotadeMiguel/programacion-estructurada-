
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

