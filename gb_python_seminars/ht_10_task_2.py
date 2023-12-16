from random import randint

a = [randint(1, 10) for x in range(10)]
b = [randint(1, 10) for x in range(10)]

testList = [[[3, 12, 8, 41, 7, 21, 9, 14, 5, 30], [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                                          0]],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]]


class LotteryGame:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        result = []
        for el in self.list1:
            if el in self.list2:
                result.append(el)
        return print(f'Совпадающие числа: {list(result)} \nКоличество совпадающих чисел: {len(result)}') if len(
            result) else print(f"Совпадающих чисел нет.")


for el in testList:
    LotteryGame(el[0], el[1]).compare_lists()
