import math


 # clase base que representa una calculadora simple )Abstraccion=
class Calculadora:
    def __init__(self, a, b):
        self._resultado = 0 # Atributo privado (Encapsulamiento)
        self.a = a
        self.b = b
        self.operacion = ""
    
    def mostrar_operacion(self):
        return f"{self.operacion}:{self.a} y {self.b} = {self._resultado}"

    def sumar(self):
        self._resultado = self.a + self.b
        self.operacion="suma"
        return self.mostrar_operacion()
    
    
    def restar(self):
        self._resultado = self.a + self.b 
        self.operacion="resta"
        return self.mostrar_operacion()

    
    def multiplicar(self):
        self._resultado = self.a * self.b 
        self.operacion="multiplicacion"
        return self.mostrar_operacion()
    
    def dividir(self):
        if self.b !=0 :
            self._resultado = self.a / self.b 
            self.operacion= "division"
            return self.mostrar_operacion()
        else:
            return "Error: Division por cero"
        
Calculadora_1 = Calculadora(15, 5)
print(Calculadora_1.sumar())

Calculadora_2 = Calculadora(20, 5)
print(Calculadora_2.restar())

print(Calculadora_1.multiplicar())

print(Calculadora_2.dividir())








 
 