from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return round(2 * pi * self.radius, 2)

    def square(self):
        return round(pi * (self.radius ** 2), 2)

    def __str__(self):
        return f'Circle with radius {self.radius}'
