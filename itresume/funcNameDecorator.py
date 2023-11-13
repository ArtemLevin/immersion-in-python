def funcNameDecorator(func):
    def wrapper(*args):
        print(f"function name: {func.__name__}")
        result = func(*args)
        return print(f"{result = }")
    return wrapper


@funcNameDecorator
def myFunc(a, b):
    return a+b
myFunc(3, 5)