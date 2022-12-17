from shape import Shape


class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b

    def get_side_a(self):
        return self.side_a

    def get_side_b(self):
        return self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def square(self):
        return self.side_a * self.side_b
