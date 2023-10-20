# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')
#
#
# my_iter = iter(factorial(10))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
for item in gen(10, 1):
    print(f'{item = }')