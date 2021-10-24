from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError
        self.a = a
        self.b = b
        self.area = (a * b)
        self.perimeter = ((a + b) * 2)
        self.name = 'Rectangle'
