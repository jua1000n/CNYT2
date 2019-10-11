# Librería que simula de lo clásico a lo cuántico 

Es una librería la cual realiza una simulacion de probablilidad cuantica, con ejemplos delas canicas, y de las multiples rendijas

# Como instalar la libreria  

Que cosas necesitas para instalar el software y como instalarlas 

Las cosas más básicas para poder usar la librería es tener Python 3.7 instalado en tu ordenador, para poder implementar la librería solo necesita crear una carpeta, guardar la librería con el nombre “ lisbre_uni3.py ”, en el programa que quieras usar la librería tienes que poner “ import lisbre_uni3”. 
 ```python
 import lib1
 ```

# Ejecución de librería 

En este caso la libreria coje matrices con numeros reales, como  con numeros complejos, en este caso el mismo programa reconoce el tipo de dato ingresado, prar que pueda leer los complejos lo mete en una tupla, y dependiendo de lo que este corriedno tiene que ingresar el numero de clicks, la matriz y el vector de clicks 
 ```python
 #Reales
  def test_accion(self):
        a=[[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,1,0,0,0,1],
           [0,0,0,1,0,0],
           [0,0,1,0,0,0],
           [1,0,0,0,1,0]]
        b=[[6],
           [2],
           [1],
           [5],
           [3],
           [10]]
 ```

Las funciones que vamos a encontrar se encuentra: 

- Experimentos con coeficiente booleanos
- Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
- Experimento de las múltiples rendijas cuántico.


# Pruebas
En estas podremos ver el tipo de entrada que recibe,y las diferentes salidas que puede votar:
```python
import unittest
import ComplejosVector

class MyTestCase(unittest.TestCase):
    def test_canic(self):
        a=[[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [1/6,1/3,0,1,0,0,0,0],
           [1/6,1/3,0,0,1,0,0,0],
           [1/3,1/3,1/3,0,0,1,0,0],
           [1/6,0,1/3,0,0,0,1,0],
           [1/6,0,1/3,0,0,0,0,1]]
        b=[[1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0]]
        d=2
        c=[[0], [0], [0], [1/6], [1/6], [1/3], [1/6], [1/6],]
        self.assertEqual(lisbre_uni3.canic(a,b,d), c)
if __name__ == '__main__':
    unittest.main()
```
# Hecho por:
- Juan Sebastian Cadavid P
- Ingeniero de Sistemas
- Escuela Colombiana de Ingeniería Julio Garavito
