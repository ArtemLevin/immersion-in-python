import fractions
from functools import reduce

def fracSum(fraction1, fraction2):
    frac1 = [int(x) for x in fraction1.split('/')]
    frac2 = [int(x) for x in fraction2.split('/')]

    def prime(num):
        primeList = []
        rangeNum = num
        if num == 1:
            primeList.append(1)
            return primeList
        else:
            while num != 1:
                i = 2
                while i <=rangeNum:
                    if num%i==0:
                        primeList.append(i)
                        num = num//i
                    else:
                        i += 1
            return primeList

    primeList1 = prime(frac1[0]*frac2[1] + frac1[1]*frac2[0])
    primeList2 = prime(frac1[1]*frac2[1])
    primeList3 = prime(frac1[0]*frac2[0])
    primeList4 = prime(frac1[1]*frac2[1])


    print(primeList1, primeList2, primeList3, primeList4)
    i = 1
    while i < 10:
        if i in primeList1 and i in primeList2:
            primeList1.remove(i)
            primeList2.remove(i)
        else:
            i+=1

    i = 1
    while i < 10:
        if (i in primeList3) and (i in primeList4):
            primeList3.remove(i)
            primeList4.remove(i)
        else:
            i+=1
    if not primeList1:
        primeList1 = [1]
    if not primeList2:
        primeList2 = [1]
    if not primeList3:
        primeList3 = [1]
    if not primeList4:
        primeList1 = [1]
    print(primeList1, primeList2, primeList3, primeList4)
    fracModSum = fractions.Fraction(fraction1) + fractions.Fraction(fraction2)
    return (f'Сумма дробей: {reduce(lambda x, y: x*y, primeList1)}/{reduce(lambda x, y: x*y, primeList2)}\n\
Произведение дробей: {reduce(lambda x, y: x*y, primeList3)}/{reduce(lambda x, y: x*y, primeList4)}\n\
Сумма дробей: {fracModSum}\n\
Произведение дробей: {fractions.Fraction(fraction1)*fractions.Fraction(fraction2)}')


print (fracSum("2/3", "3/4"))