from functools import reduce

# the sieve of Eratosthenes
# n = 100
# primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))
# print(primes)

# Fibonacci
# n =100
# fib = reduce(lambda x, _: x + [x[-2] + x[-1]], [0]*(n-2), [0,1])
# print(fib)

# binnary search
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# x = 15
#
# bs = lambda x, l, lo, hi: -1 if lo > hi else \
#     (lo + hi) // 2 if l[(lo + hi) // 2] == x else \
#         bs(x, l, lo, (lo + hi) // 2) if l[(lo + hi) // 2] > x else \
#             bs(x, l, (lo + hi) // 2, hi)
#
# print(bs(x, l, 0, len(l) - 1))
