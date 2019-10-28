from unittest import TestCase
from codigo_avulso_test_tutorial.quadrado import Quadrado

class TestQuadrado(TestCase):
    
    def setUp(self):
        """Classe configura os parametros de teste
        """
        super(TestQuadrado, self).setUp()

        self.fig = Quadrado()

    def test_init(self):

        fig = Quadrado(lado=15)
        self.assertEqual(fig.lado, 15)

        fig = Quadrado()
        self.assertEqual(fig.lado, 0)

    def test_init_error(self):

        with self.assertRaises(TypeError):
            fig = Quadrado(lado='XPTO')

        with self.assertRaises(ValueError):
            fig = Quadrado(lado=-5)

    def test_get_area(self):
        self.fig.lado = 2
        self.assertEqual(self.fig.get_area(), 4)

        self.fig.lado = 7.0
        self.assertEqual(self.fig.get_area(), 49.0)
        
    def test_get_perimetro(self):
        self.fig.lado = 2
        self.assertEqual(self.fig.get_perimetro(), 8)

        self.fig.lado = 7.0
        self.assertEqual(self.fig.get_perimetro(), 28.0)
