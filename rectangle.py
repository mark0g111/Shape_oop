from mixin_rectangle import MixinRectangle
from shape import Shape


class Rectangle(Shape, MixinRectangle):

    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a > 0 and side_b > 0:
            self.__side_a = side_a
            self.__side_b = side_b
        else:
            raise ValueError('Sides value must be over zero!')

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, new_value):
        self.__side_a = new_value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, new_value):
        self.__side_b = new_value

    def perimeter(self):
        return super().perimeter(self.side_a, self.side_b)

    def square(self):
        return self.__side_a * self.__side_b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return other.__side_a == self.__side_a and other.__side_b == self.__side_b
        return False

    def __repr__(self):
        return f'Rectangle({self.__side_a}, {self.__side_b})'

    def __str__(self):
        return f'Rectangle with sides {self.__side_a} and {self.__side_b}'
