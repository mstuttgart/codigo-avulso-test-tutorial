from .figura_geometrica import FiguraGeometrica


class Quadrado(FiguraGeometrica):

    def __init__(self, lado=0):

        if type(lado) not in [int, float]:
            raise TypeError('Tipo incorreto')

        if lado < 0:
            raise ValueError('Somente valores positivos')

        self.lado = lado

    # Retorna a area do quadrado
    def get_area(self):
        return self.lado ** 2

    # Retorna o perimetro do quadrado
    def get_perimetro(self):
        return 4 * self.lado
