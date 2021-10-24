from src.Figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, a, b, c, p):
        if c <= 0 or a <= 0 or b <= 0:
            raise ValueError
        elif ((a + c) < b) or ((c + b) < a) or ((a + b) < c):
            raise ValueError
        self.c = c
        self.a = a
        self.b = b
        self.area = sqrt(p * (p - a) * (p - b) * (p - c))
        self.perimeter = (a + b + c)
        self.name = 'Triangle'

    def semiperimeter(self):
        p = (self.a + self.b + self.c)/2
        return p
