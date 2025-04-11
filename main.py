from calculadorapoo import Calculadora
from factorialpoo import CalculadoraFactorial

print("Calculadora Estandar")
Calculadora_1 = Calculadora()

print(Calculadora_1.sumar(2, 5))
print(Calculadora_1.restar(10, 9))
print(Calculadora_1.multiplicar(5, 9))
print(Calculadora_1.dividir(150, 6))

print("Calculadora Factorial")
calculadora_factorial = CalculadoraFactorial(numero=5)
print(calculadora_factorial.calcular())


