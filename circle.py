from math import pi


class Circle:

    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('Radius must be over zero!')

    def length(self):
        return round(2 * pi * self.radius, 2)

    def square(self):
        return round(pi * (self.radius ** 2), 2)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return other.radius == self.radius
        return False

    def __repr__(self):
        return f'Circle({self.radius})'

    def __str__(self):
        return f'Circle with radius {self.radius}'
