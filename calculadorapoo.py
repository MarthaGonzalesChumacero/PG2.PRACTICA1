import math


 # clase base que representa una calculadora simple )Abstraccion=
class Calculadora:
    def __init__(self):
        self.__resultado = 0 
        self.operacion = ""

    def sumar(self, a, b):
        self.operacion= "Suma"
        self.__resultado = a + b
        return self.mostrar_operacion(a, b)
    
    def restar(self, a, b):
        self.operacion="Resta"
        self.__resultado = a - b
        return self.mostrar_operacion(a, b)

    def _multiplicar(self, a, b):
        return a * b
    
    def multiplicar(self, a, b):
        self.operacion="Multiplicar"
        self.__resultado = self._multiplicar(a, b)
        return self.mostrar_operacion(a, b)
    
    def dividir(self, a, b):
        self.operacion = "Dividir"
        if b != 0:
            self.__resultado = a / b	
            return self.mostrar_operacion(a, b)
        else:
            return "Error: Division por cero"
    def mostrar_operacion(self, a, b):
        return f"{self.operacion}: {a} y {b} = {self.__resultado}"








 
 