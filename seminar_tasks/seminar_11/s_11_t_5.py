# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle():
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width


    def square(self):
        if 0 in (self.length, self.width):
            for el in (self.length, self.width):
                if el!=0: return el**2
        else: return self.length*self.width

    def perimeter(self):
        return 2*(self.length + self.width)

    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())