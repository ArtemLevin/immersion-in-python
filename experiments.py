
def funcCounter(func):
    counter = 0

    def wrapper(*args):
        nonlocal counter
        result = func(*args)
        counter += 1
        return f" result_{counter} = {result}"

    return wrapper


@funcCounter
def func(a, b):
    x = a + b
    return x


for a in range(4):
    for b in range(4):
        print(func(a, b))
