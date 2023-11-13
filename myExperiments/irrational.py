

def irrational(num):
    min_coeff = 1000000
    final_res = []
    coeff_dict = {}
    for a in range(-10, 11):
        for b in range(10**2):
            if (a,b) in coeff_dict.keys():
                a_b_part = coeff_dict[(a,b)]
            else: a_b_part = a * (b ** 0.5)
            for c in range(-10, 11):
                for d in range(10**2):
                    c_d_part = c * (d ** 0.5)
                    coeff_dict[(c, d)] = c_d_part
                    for e in range(-10**2, 10**2):
                        try:
                            if abs((a_b_part + c_d_part) / e - num) < 1e-10:
                                res = [a, b, c, d, e]
                                sum_coeff = sum([abs(x) for x in res])
                                if sum_coeff < min_coeff:
                                    min_coeff = sum_coeff
                                    final_res = res
                        except ZeroDivisionError:
                            pass
    if final_res:
        if 0 in (final_res[0], final_res[1]):
            return f"({final_res[2]:+}*sqrt{final_res[3]})/({final_res[4]})"
        elif 0 in (final_res[2], final_res[3]):
            return f"{final_res[0]}*sqrt{final_res[1]}/({final_res[4]})"
        else:
            return f"({final_res[0]}*sqrt{final_res[1]}{final_res[2]:+}*sqrt{final_res[3]})/({final_res[4]})"


if __name__ == "__main__":
    print(irrational(2**0.5))
