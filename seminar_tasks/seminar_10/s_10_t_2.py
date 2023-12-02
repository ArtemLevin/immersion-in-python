class Rectangle():
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width


    def square(self):
        if 0 in (self.length, self.width):
            for el in (self.length, self.width):
                if el!=0: return el**2
        else: return self.length*self.width

newRect  = Rectangle(12)

print(f"{newRect.square()}")