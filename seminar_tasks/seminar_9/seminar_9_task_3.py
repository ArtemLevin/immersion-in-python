# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции
import inspect
import json


def funcParametersResultToJson(myFunc):
    def wrapper(*args, **kwargs):
        parameters = list(zip(inspect.getfullargspec(myFunc)[0], args))
        funcDict = {}
        for el in parameters:
            funcDict[el[0]] = el[1]
        funcDict["result"] = myFunc(*args)
        with open(f"{myFunc.__name__}.json", "a") as f:
            json.dump(funcDict, f)
        return print(funcDict)

    return wrapper


a, b, c = 1, 2, 3


@funcParametersResultToJson
def myFunc(a, b, c):
    return a + b + c
myFunc(a,b,c)
