from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        if a <= 0:
            raise ValueError
        self.a = a
        self.area = (a ** 2)
        self.perimeter = (a * 4)
        self.name = 'Square'