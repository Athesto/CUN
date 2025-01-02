#!/usr/bin/env python3

import unittest
from unittest.mock import patch

# Ejercicio 3a: Determinar si el numero es positivo, cero o negativo
def solution_3a():
    item = input("Enter a number: ")
    if int(item) > 0:
        return 'positive'
    elif int(item) == 0:
        return 'zero'
    return 'negative'

# Ejercicio 3b: Determinar el IMC
def solution_3b():
    weight = float(input("Peso (kg): "))
    height = float(input("Altura (m): "))
    imc = "{:.2f}".format(weight / height**2)
    imc = float(imc)
    if imc < 18.5:
        message = 'Bajo peso'
    elif imc < 25:
        message = "Peso normal"
    elif imc < 30:
        message = "Sobrepeso"
    else:
        message = "Obesidad"
    return {
        'imc': imc,
        'message': message
    }

# Ejercicio 3c: Calcular el factorial de un numero
def solution_3c(number):
    if number == 0:
        return 1
    for i in range(1, number):
        number *= i
    return number

# Ejercicio 3d: tabla de multiplicar
def solution_3d():
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
    @patch('builtins.input', side_effect=['1', '0', '-1'])
    def test_3a(self, mock_input):
        self.assertEqual(solution_3a(), 'positive')
        self.assertEqual(solution_3a(), 'zero')
        self.assertEqual(solution_3a(), 'negative')

    @patch('builtins.input', side_effect=[
        '60', '2',
        '80', '2',
        '100', '2',
        '160', '2',
    ])
    def test_3b(self, mock_input):
        self.assertEqual(solution_3b(), {'imc': 15.0, 'message': 'Bajo peso'})
        self.assertEqual(solution_3b(), {'imc': 20.0, 'message': 'Peso normal'})
        self.assertEqual(solution_3b(), {'imc': 25.0, 'message': 'Sobrepeso'})
        self.assertEqual(solution_3b(), {'imc': 40.0, 'message': 'Obesidad'})

    def test_3c(self):
        self.assertEqual(solution_3c(5), 120)
        self.assertEqual(solution_3c(0), 1)

    def test_3d(self):
        self.assertEqual(solution_3d(), None)


if __name__ == '__main__':
    unittest.main(exit=False)
