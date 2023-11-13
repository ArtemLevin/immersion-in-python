
res = []
for a in range(-100, 101):
    for b in  range(-100, 101):
        for c in  range(-100, 101):
            for d in range(-100, 101):
                for e in range(-100, 101):
                    x_list = []
                    for x in [x/100.0 for x in range(-100, 101)]:
                        try:
                            if ((a/(x**2-b)) - (c-d*x)/(x**3+b)-(e/(x**2+x+b))) == 0:
                                x_list.append(x)
                        except ZeroDivisionError:
                            pass
                    res.append([a, b, c, d, e, x_list])
                    print ([a, b, c, d, e, x_list]) if len(x_list) > 1 else None
# for el in res:
#     if len(el[4]) == 2:
#         print(el)