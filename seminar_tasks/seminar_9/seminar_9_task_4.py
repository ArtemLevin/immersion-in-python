def runCounter(myFunc):
    counter = 0
    def wrapper(*args):
        nonlocal counter
        counter += 1
        if counter <= 3:
            result = myFunc(*args)
            return result
        else:
            print("Run limit exceeded")
            return True
    return wrapper

@runCounter
def func_1():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return print(f"result = {a + b}")

