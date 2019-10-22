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
        c=[[0], [0], [12], [5], [1], [9]]
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
    #3 Experimento de las múltiples rendijas cuántico.
    def test_cuan(self):
        a = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
        b = [[(6,0)],[(2,0)],[(1,0)],[(5,0)],[(3,0)],[(10,0)]]
        c = 1
        esperado = [[(0, 0)], [(0, 0)], [(12, 0)], [(5, 0)], [(1, 0)], [(9, 0)]]
        self.assertEqual(lib1.canic(a,b,c), esperado)


if __name__ == '__main__':
    unittest.main()
