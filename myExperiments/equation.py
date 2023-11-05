import math


def bigGoodDiscr():
    quadro = [x**2 for x in range(10**3)]
    koeff = []
    for a in range(1, 200):
        for b in range(150, 200):
            for c in range(1, 200):
                discr = b**2 - 4*a*c
                if discr in quadro and discr%100 != 0 and abs(math.sqrt(discr)-b) in (range(11)): koeff.append([a, b, c, discr])
    return koeff

myEqCoeff = bigGoodDiscr()


with open("quadro.txt", "a", encoding="utf-8") as f:
    counter = 1
    for el in myEqCoeff:
        print(f'{counter}) {el[0]}*x^2{el[1]:+}*x{el[2]:+} = 0 (D = {el[3]})', file = f)
        counter+=1