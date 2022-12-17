from rectangle import Rectangle


class Quadrate(Rectangle):

    def __init__(self, side_a):
        super().__init__(side_a, side_a)

    def __str__(self):
        return f'Quadrate with sides {self.side_a}'
