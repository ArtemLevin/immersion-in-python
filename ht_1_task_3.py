list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 11, 12, 13, 14, 15, 16]

def match(list1, list2):
    return print(f"Количество совпадающих чисел: {2*len(list1) - len(set(list1 + list2))}")

match(list1, list2)