# Desarrolla un script en Python que simule el funcionamiento de una tienda de libros en línea. Tu objetivo es crear un 
# sistema de gestión de inventario que permita a los usuarios agregar nuevos libros, buscar libros existentes por título y 
# registrar ventas.
#  You
#  Para lograr esto, sigue las siguientes especificaciones:
#  1. Define una clase llamada Libro que represente un libro en la tienda. Esta clase debe tener tres atributos: titulo, 
# autor y precio. Implementa un método __init__ para inicializar estos atributos cuando se crea una nueva 
# instancia de la clase.
#  2. Crea una clase llamada Inventario que gestione el inventario de la tienda. Esta clase debe tener los siguientes 
# métodos:
#  ◦ __init__: Inicializa una lista vacía para almacenar los libros en el inventario.
#  ◦ agregar_libro(libro): Recibe un objeto de la clase Libro y lo agrega al inventario.
#  ◦ buscar_libro(titulo): Recibe el título de un libro como argumento y busca en el inventario un libro con 
# ese título. Si lo encuentra, muestra la información del libro (título, autor y precio). Si no lo encuentra, muestra 
# un mensaje indicando que el libro no está en el inventario.
#  ◦ registrar_venta(titulo): Recibe el título de un libro vendido y actualiza el inventario eliminando el libro 
# vendido. También muestra un mensaje confirmando la venta y actualiza el total de ventas.
#  Customer Success
#  NOT FOR DISTRIBUTION © Abdessamad Ammi bcloud.consulting
#  30
# Programación
#  3. Implementa una función principal llamada main() que permita al usuario interactuar con el sistema. En esta 
# función, proporciona un menú con las siguientes opciones:
#  ◦ Agregar un nuevo libro al inventario.
#  ◦ Buscar un libro por título.
#  ◦ Registrar una venta de un libro

class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.libros = []
        self.total_ventas = 0.0

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado al inventario.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print("Libro encontrado:")
                print(libro)
                return libro
        print("Libro no encontrado en el inventario.")
        return None

    def registrar_venta(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                self.total_ventas += libro.precio
                print(f"Venta registrada: '{libro.titulo}' vendido por ${libro.precio:.2f}.")
                print(f"Total de ventas: ${self.total_ventas:.2f}")
                return
        print("No se pudo registrar la venta. El libro no está en el inventario.")


def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de la Tienda de Libros ---")
        print("1. Agregar un nuevo libro")
        print("2. Buscar un libro por título")
        print("3. Registrar una venta")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            while True:
                try:
                    precio = float(input("Precio del libro: "))
                    break
                except ValueError:
                    print("Por favor, ingresa un valor numérico válido para el precio.")
            libro = Libro(titulo, autor, precio)
            inventario.agregar_libro(libro)

        elif opcion == '2':
            titulo = input("Título del libro a buscar: ")
            inventario.buscar_libro(titulo)

        elif opcion == '3':
            titulo = input("Título del libro vendido: ")
            inventario.registrar_venta(titulo)

        elif opcion == '4':
            print("Gracias por usar la tienda de libros. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
