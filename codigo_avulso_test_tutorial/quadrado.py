# -*- coding: utf-8 -*-
from figura_geometrica import FiguraGeometrica

class Quadrado(FiguraGeometrica):

    def __init__(self):
      self.lado = 0

    # Retorna a area do quadrado
    def get_area(self):
        return self.lado**2

    # Retorna o perimetro do quadrado
    def get_perimetro(self):
        return 4 * self.lado

