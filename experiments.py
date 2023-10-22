from functools import reduce

n = 5
myList = reduce(lambda x, y: x + [x[-1] - x[-2]], [0]*(n+1), [3, 7])
print(myList)

