class Figure:
    name = None
    area = None
    perimeter = None

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            sum_areas = self.area + other_figure.area
            return sum_areas
        else:
            raise ValueError("Wrong class passed")
