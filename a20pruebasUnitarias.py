import unittest
from io import StringIO
from unittest.mock import patch
from a2variablesYAmbito import modificar_global, mensaje_global
from a5funcionesProcedimientos import sumar, duplicar_valorN, agregar_elemento
from a6recursividad import factorial
from a13usoEnumerados import DiasSemana, mostrar_dia 
from a16manejoListasTuplas import calcular

class TestFuncionesProcedimientos(unittest.TestCase):

    # Pruebas para la función sumar
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

    # Pruebas para duplicar_valorN
    def test_duplicar_valorN(self):
        self.assertEqual(duplicar_valorN(5), 10)
        self.assertEqual(duplicar_valorN(-3), -6)
        self.assertEqual(duplicar_valorN(0), 0)

    # Pruebas para agregar_elemento
    def test_agregar_elemento(self):
        lista = [1, 2, 3]
        agregar_elemento(lista)
        self.assertIn("Nuevo elemento", lista)
        self.assertEqual(len(lista), 4)

class TestDiasSemana(unittest.TestCase):

    def test_dia_valido(self):
        # Probamos que el valor 1 corresponde a LUNES
        dia = DiasSemana(1)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            mostrar_dia(dia)
            self.assertIn("El día seleccionado es: LUNES", mock_stdout.getvalue())

    def test_dia_invalido(self):
        # Probamos que se maneja correctamente un valor fuera del rango
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            mostrar_dia(None)  # Llamamos a mostrar_dia con None
            self.assertIn("El valor no corresponde a un día de la semana.", mock_stdout.getvalue())

    def test_mostrar_dia_invalido(self):
        # Probamos con un número fuera del rango de la enumeración
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            mostrar_dia(None)  # Llamamos a mostrar_dia con None
            self.assertIn("El valor no corresponde a un día de la semana.", mock_stdout.getvalue())

    def test_dia_orden_correcto(self):
        # Aseguramos que los días están en el orden correcto
        dias_orden = list(DiasSemana)
        self.assertEqual(dias_orden[0], DiasSemana.LUNES)
        self.assertEqual(dias_orden[6], DiasSemana.DOMINGO)

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=StringIO)
    def test_seleccionar_dia_valido(self, mock_stdout, mock_input):
        # Probamos que se selecciona correctamente un día de la semana a partir de la entrada del usuario
        valor = int(mock_input())
        dia_seleccionado = DiasSemana(valor)
        mostrar_dia(dia_seleccionado)
        self.assertIn("El día seleccionado es: MIERCOLES", mock_stdout.getvalue())

    @patch("builtins.input", return_value="8")
    @patch("sys.stdout", new_callable=StringIO)
    def test_seleccionar_dia_invalido(self, mock_stdout, mock_input):
        valor = int(mock_input())
        try:
            dia_seleccionado = DiasSemana(valor)
        except ValueError:
            dia_seleccionado = None
        mostrar_dia(dia_seleccionado)
        self.assertIn("El valor no corresponde a un día de la semana.", mock_stdout.getvalue())


# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
