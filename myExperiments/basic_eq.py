import fractions
from myExperiments.irrational import irrational
import math


def funcCounter(func):
    counter = 0

    def wrapper(*args):
        nonlocal counter
        result = func(*args)
        if result:
            counter += 1
            return print(f"result_{counter} = {result[0]} = {result[1]}") if result[1] else print(
                f"result_{counter} = {result[0]}")

    return wrapper


def myEquation(t, k, x):
    result = (x+7)/(x+6) - x**3
    return result


@funcCounter
def findRoot(a, b, t, k, myFunc):
    if abs(a - b) < 1e-10:
        return (a, irrational(a))
    try:
        if myFunc(t, k, a) * myFunc(t, k, b) <= 0:
            average = (a + b) / 2
            if myFunc(t, k, a) * myFunc(t, k, average) <= 0:
                findRoot(a, average, t, k, myFunc)
            elif myFunc(t, k, b) * myFunc(t, k, average) < 0:
                findRoot(average, b, t, k, myFunc)
    except (ZeroDivisionError, ValueError, TypeError):
        pass




def findSolvation():
    for t in range(-10, 11):
        for k in range(-10, 11):
            print(f"{t=}, {k=}")
            area = [x / 1000.0 for x in range(-100000, 100000)]
            for i in range(len(area) - 1):
                findRoot(area[i], area[i + 1], t, k,  myEquation)



findSolvation()