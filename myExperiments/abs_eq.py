abs_coeff = []

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            for d in range(1, 31):
                if (abs(4 + 2 * a + b) == c * 2 + d) and (abs(9 + 3 * a + b) == c * 3 +d):
                    abs_coeff.append([a, b, c, d])

with open("abs_coeff.txt", "w") as f:
    counters = 1
    for e in abs_coeff:
        print(f'{counters}) |x^2{e[0]:+}*x{e[1]:+}| = {e[2]:}*x{e[3]:+}', file=f)
        counters += 1
