def fibonacci():
    n = 0
    result = [0, 1]
    if n == 0:
        n +=1
        yield result[0]

    if n == 1:
        n+=1
        yield result[1]

    while True:
        number = result[i - 1] + result[i - 2]
        result.append(number)
        n+=1
        yield number

f = fibonacci()
for i in range(10):
    print(next(f))
