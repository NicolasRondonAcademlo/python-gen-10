# this
from typing import Union, Optional
import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset point position to
        x = 0
        y = 0
        """
        self.x = 0
        self.y = 0

    def move(self, x: Union[int, float], y: Union[int, float]) -> None:
        """
        Move point to
        x: x
        y: y
        """
        if isinstance(x, int) or isinstance(x, float):
            self.x = x
        if isinstance(y, int) or isinstance(y, float):
            self.y = y
        else:
            raise TypeError("Debe ser un flotante o un entero")

    def calculate_distance(self, other_point) -> float:
        """
        Calculate distance between points
        """
        return math.sqrt(
            (self.x - other_point.x) ** 2
            +
            (self.y - other_point.y) ** 2
        )


p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6
# print(p1.x, p1.y)
# print(p2.x, p2.y)

p = Point()
p.reset()
# print(p.x, p.y)

p3 = Point()
p3.x = 5
p3.y = 6

# print(p3.x, p3.y)
# p3.reset()
# print(p3.x, p3.y)
#
# p4 = Point()
# p4.reset()
# print(p4.x, p4.y)

p5 = Point()
p5.reset()
p5.move(5, 7)

p6 = Point()
p6.reset()

distance = p6.calculate_distance(p5)

p7 = Point()
print(p7.x, p7.y)


class Calcular:

    @classmethod
    def suma(cls, x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y


a = Calcular.suma(3, 3)
print(a)


# Encapsulamiento ->