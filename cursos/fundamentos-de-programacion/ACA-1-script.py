#!/usr/bin/env python3

import unittest
from unittest.mock import patch

# Ejercicio 3a: Determinar si el numero es positivo, cero o negativo
def classify_number():
    data_input = input("Enter a number: ")
    try:
        number = float(data_input)
    except ValueError:
        # Si no se puede convertir a número, determinar si es texto o algo más
        if data_input.isalpha():
            print("Error: You entered a string: '" + data_input + "' Expected a number.")
        else:
            print("Error: You entered something else: '" + data_input + "' Expected a number.")
        return 'Error'
    if number > 0:
        return 'positive'
    elif number == 0:
        return 'zero'
    return 'negative'

# Ejercicio 3b: Determinar el IMC
def get_imc():
    try: 
        weight = float(input("Peso (kg): "))
        height = float(input("Altura (m): "))
        imc = "{:.2f}".format(weight / height**2)
        imc = float(imc)
    except ValueError:
        print("Error: You entered something else:") 
        return "Error"

    if imc < 18.5:
        message = 'Bajo peso'
    elif imc < 25:
        message = "Peso normal"
    elif imc < 30:
        message = "Sobrepeso"
    elif imc < 34.9:
        message = "Obesidad I"
    elif imc < 39.9:
        message = "Obesidad II"
    elif imc < 49.9:
        message = "Obesidad III"
    else:
        message = "Obesidad IV"
    return {
        'imc': imc,
        'message': message
    }

# Ejercicio 3c: Calcular el factorial de un numero
def get_factorial(number):
    if number == 0:
        return 1
    for i in range(1, number):
        number *= i
    return number

# Ejercicio 3d: tabla de multiplicar
def mutiplication_table():
    multiplier = 1
    multiplicand = 0
    while multiplier <= 10:
        print("")
        while multiplicand <= 10:
            print(f"{multiplier:02} x {multiplicand:02} = {multiplier*multiplicand:3}")
            multiplicand += 1
        multiplicand = 0
        multiplier += 1

class Tests(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '0', '-1', "hello world"])
    def test_3a(self, mock_input):
        self.assertEqual(classify_number(), 'positive')
        self.assertEqual(classify_number(), 'zero')
        self.assertEqual(classify_number(), 'negative')
        self.assertEqual(classify_number(), 'Error')

    @patch('builtins.input', side_effect=[
        '60', '2',
        '80', '2',
        '100', '2',
        '160', '2',
        "hello world", "2",
    ])
    def test_3b(self, mock_input):
        self.assertEqual(get_imc(), {'imc': 15.0, 'message': 'Bajo peso'})
        self.assertEqual(get_imc(), {'imc': 20.0, 'message': 'Peso normal'})
        self.assertEqual(get_imc(), {'imc': 25.0, 'message': 'Sobrepeso'})
        self.assertEqual(get_imc(), {'imc': 40.0, 'message': 'Obesidad III'})
        self.assertEqual(get_imc(), "Error") 

    def test_3c(self):
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(0), 1)

    def test_3d(self):
        self.assertEqual(mutiplication_table(), None)


if __name__ == '__main__':
    unittest.main(exit=False)
