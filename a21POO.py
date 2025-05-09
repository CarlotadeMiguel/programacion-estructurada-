class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True
        return f"El coche {self.marca} {self.modelo} está encendido."

    def apagar(self):
        self.encendido = False
        return f"El coche {self.marca} {self.modelo} está apagado."

    def estado(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"El coche {self.marca} {self.modelo} está {estado}."

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020)
mi_cocheD = Coche("Dacia", "Lodgy", 2014)

# Usar métodos del objeto
print(mi_coche.encender())   # El coche Toyota Corolla está encendido.
print(mi_coche.estado())     # El coche Toyota Corolla está encendido.
print(mi_coche.apagar())     # El coche Toyota Corolla está apagado.

print(mi_cocheD.encender())   # El coche Toyota Corolla está encendido.
print(mi_cocheD.estado())     # El coche Toyota Corolla está encendido.
print(mi_cocheD.apagar())     # El coche Toyota Corolla está apagado.
