# -*- coding: utf-8 -*-
from unittest import TestCase
from codigo_avulso_test_tutorial.quadrado import Quadrado

class TestQuadrado(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.fig = Quadrado()

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
