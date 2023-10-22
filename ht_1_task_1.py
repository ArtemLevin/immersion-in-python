a, b, c = [int(x) for x in input("Enter the data separated by a space -----> ").split()]
sideList = [a, b, c]


def triangle(sideList):
    for i in range(len(sideList)):
        sideSum = 0
        for j in range(len(sideList)):
            if i != j:
                sideSum += sideList[j]
        if sideList[i] >= sideSum: return print("Треугольник не существует")
    if len(set(sideList)) == 1:
        return print("Треугольник существует" + "\n" + "Треугольник равносторонний")
    elif len(set(sideList)) == 2:
        return print("Треугольник существует" + "\n" + "Треугольник равнобедренный")
    elif len(set(sideList)) == 3:
        return print("Треугольник существует" + "\n" + "Треугольник разносторонний")


triangle(sideList)
