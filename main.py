import pickle
from quadrate import Quadrate
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

rectangle = Rectangle(2, 3)
quadrate = Quadrate(4)
triangle = Triangle(3, 4, 5)
circle = Circle(5)

print(rectangle)

with open('rectangle.pickle', 'wb') as file:
    pickle.dump(rectangle, file)

with open('rectangle.pickle', 'rb') as file:
    rectangle_2 = pickle.load(file)

print(rectangle_2)
print(rectangle == rectangle_2)
