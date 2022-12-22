class MixinRectangle:
    def perimeter(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        return 2 * (self.side_a + self.side_b)
