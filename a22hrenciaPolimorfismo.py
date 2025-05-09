# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

    def describir(self):
        return f"Soy un animal llamado {self.nombre}."

    def moverse(self):
        return "Me estoy moviendo de una manera genérica."

# Subclase 1
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

    def describir(self):
        return f"Soy un perro llamado {self.nombre}."


# Subclase 2
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

    def describir(self):
        return f"Soy un gato llamado {self.nombre}."

    def moverse(self):
        return "Me deslizo sigilosamente."

# Subclase 3
class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío pío"

    def describir(self):
        return f"Soy un pájaro llamado {self.nombre}."

    def moverse(self):
        return "Vuelo alto en el cielo."

# Función que demuestra polimorfismo
def mostrar_informacion(animal):
    print(animal.describir())
    print(f"Sonido: {animal.hacer_sonido()}")
    print(f"Movimiento: {animal.moverse()}")

# Crear instancias de las clases
animales = [
    Perro("Rex"),
    Gato("Michi"),
    Pajaro("Piolín"),
    Animal("Genérico")
]

# Iterar sobre las instancias y demostrar polimorfismo
for animal in animales:
    mostrar_informacion(animal)
    print("-" * 30)