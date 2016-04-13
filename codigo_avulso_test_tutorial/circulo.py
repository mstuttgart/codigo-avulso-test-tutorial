# -*- coding: utf-8 -*-
import math
from figura_geometrica import FiguraGeometrica

class Circulo(FiguraGeometrica):

    def __init__(self):
      self.raio = 0

    # Retorna a area do circulo
    def get_area(self):
        return math.pi * self.raio**2

    # Retorna o perimetro do circulo
    def get_perimetro(self):
        return 2 * math.pi * self.raio

