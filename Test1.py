import unittest
import lib1

class MyTestCase(unittest.TestCase):
    #1. Los experimentos de la canicas con coeficiente booleanos
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
        d=1
        c=[[0], [0], [9], [5], [12], [1]]
        self.assertEqual(lib1.canic(a,b,d), c)
    #2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
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
        self.assertEqual(lib1.canic(a,b,d), c)

if __name__ == '__main__':
    unittest.main()
