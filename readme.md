---

# Practica 1: Implementacion de una calculadora en Python
En esta practica, se implementara una calculadora en Python con capacidad para realizar operaciones matematicas basicas como suma, resta, multiplicacion y division. Ademas, se extiende su funcionalidad para calcular el factorial de un numero, aplicando conceptos de herencia y polimorfismo.

## Preparacion del entorno y ejecucion

Clonar el repositorio:

```sh
git clone https://github.com/MarthaGonzalesChumacero/PG2.PRACTICA1.git
```

Crear un entorno virtual:  

```sh
python -m venv env
```

Activar el entorno virtual:  

En Windows:  

```sh
.\env\Scripts\activate
```  

En Linux o Mac:  

```sh
source env/bin/activate
```

Ejecutar el script:  

```sh
python main.py
```

Desactivar el entorno virtual:  

```sh
deactivate
```

## Implementacion de calculadora con `main`
1. **Importa la clase** CalculadoraFactorial:
   ```python
   from calculadora_poo import CalculadoraFactorial
   ```
2. **Establecer un numero y activar la calculadora de factorial** Dentro del bloque principal:
   ```python
   if __name__ == "__main__":
       calculadora_factorial = CalculadoraFactorial(5)
       print(calculadora_factorial.calculadora())
   ```
3. **Ejecuta el código** y observa el resultado del factorial directamente en la consola.

## Clases y sus funciones
## `Calculadora`
Es la Clase base que representa una calculadora basica capaz de realizar operaciones comunes como sumar, restar, multiplicar y dividir.

`Funciones`:

- sumar(a, b): Retorna la suma de a y b.
- restar(a, b): Retorna la resta de a y b.
- multiplicar(a, b): Retorna la multiplicación de a y b.
- dividir(a, b): Retorna la división de a entre b.
- mostrar_resultado(a, b): Muestra el resultado de la operación.

### Uso  

```python
from calculadora_poo import Calculadora  

calculadora_1 = Calculadora()  
print(calculadora_1.sumar(5, 6))  
print(calculadora_1.restar(15, 8))  
print(calculadora_1.multiplicar(65, 6))  
print(calculadora_1.dividir(565, 65))  
```
### `CalculadoraFactorial`
Clase que hereda `Calculadora` para calcular el **factorial** de un valor numérico.

## Métodos clave:
- calculadora(): Realiza el cálculo del factorial del número dado.
- mostrar_resultado(): Retorno el resultado del cálculo factorial.

### Uso  

```python
from factorial_poo import CalculadoraFactorial  

cal_factorial1 = CalculadoraFactorial(5)  
print(cal_factorial1.calcular())  
```
## Autor
Este código fue creado con el objetivo de facilitar el calculo de factoriales utilizando principios de **Programacion Orientada a Objetos** aprovechando los beneficios del concepto de **herencia en POO** dentro de este enfoque.

## Licencia


---