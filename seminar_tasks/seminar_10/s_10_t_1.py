import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        length = self.radius*2*math.pi
        return length

    def square(self):
        square = self.radius*(math.pi)**2
        return square


newCircle = Circle(10)
print(f"{newCircle.length() = :.3f}, {newCircle.square() = :.3f}")
