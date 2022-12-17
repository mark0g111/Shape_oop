from shape import Shape
from math import sqrt


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def __str__(self):
        return f'Triangle with sides {self.side_a}, {self.side_b} and {self.side_c}'
