from calculadorapoo import Calculadora


 # clase base que representa una calculadora simple )Abstraccion=
class CalculadoraFactorial(Calculadora):
    def __init__(self, numero):
        self.numero = numero
        super().__init__()

    def calcular(self):
        self.operacion = "Factorial"
        factorial = 1
        cont = 1
        while cont <= int(self.numero):
            factorial = self._multiplicar(factorial, cont)
            cont += 1
        self._resultado = factorial
        return self._mostrar_operacion()
    
    def _mostrar_operacion(self):
        return f"{self.operacion}: {self.numero} = {self._resultado}"