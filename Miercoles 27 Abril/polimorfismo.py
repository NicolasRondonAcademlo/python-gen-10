
# Shape
# Square - Rectangle - Circle - Diamond - Polygon - Triangle

class Shape2D:
    def __init__(self) -> None:
        self.sides = 0

    def get_area(self):
        pass

    def get_dimension(self):
        return 2

class Rectangle(Shape2D):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.sides = 4

    def get_area(self):
        return self.width * self.height


class Circle(Shape2D):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__()

    def get_area(self):
        return self.radius ** 2 * 3.14

shapes = [Rectangle(10, 20), Circle(5)]
print("Area rectangle: ", shapes[0].get_area())
print("Area circle: ", shapes[1].sides)