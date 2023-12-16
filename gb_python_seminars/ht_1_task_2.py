import math
num = int(input("enter the number "))

def isPrime(num):
    if num <= 0 or num > 10**5: return print("Invalid number")
    else:
        count = 0
        for i in range(2, round(math.sqrt(num)) + 1):
            if num%i == 0: count += 1
            if count > 0: return print("Is not prime")

    return print("Prime")

isPrime(num)
