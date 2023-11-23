from random import randint


class Lottery:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def equal_numbers(self):
        result = set(self.list1).intersection(set(self.list2))
        return f"Совпадающие числа: {list(result)}, \nКоличество совпадающих чисел: {len(result)}" if len(result) else "Совпадающих чисел нет"


a = [randint(1, 10) for x in range(10)]
b = [randint(1, 10) for x in range(10)]
print(a, b)

lot = Lottery(a, b)
print(lot.equal_numbers())