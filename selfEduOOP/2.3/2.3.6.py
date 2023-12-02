class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) == float:
            instance.__dict__[self.name] = value
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, n, m):

        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]



table = TableSheet(5,3)
num = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = num
        num += 1.0