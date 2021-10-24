from math import pi
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        if r <= 0:
            raise ValueError
        self.r = r
        self.area = (pi * (r ** 2))
        self.perimeter = (2 * r * pi)
        self.name = 'Circle'