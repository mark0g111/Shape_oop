from abc import ABC
from abc import abstractmethod


class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass
