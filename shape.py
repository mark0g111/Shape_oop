from abc import ABC
from abc import abstractmethod


class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def square(self):
        pass
