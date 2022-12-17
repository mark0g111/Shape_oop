from shape import Shape


class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

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
        return 2 * (self.__side_a + self.__side_b)

    def square(self):
        return self.__side_a * self.__side_b

    def __str__(self):
        return f'Rectangle with sides {self.__side_a} and {self.__side_b}'
