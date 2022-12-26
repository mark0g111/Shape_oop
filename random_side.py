import random


class RandomSide:

    @classmethod
    def randoms(cls, min, max, n):
        for i in range(n):
            yield random.randint(min, max)
