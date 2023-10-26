def almoust_factorial(n):
    symbols = ["*", "/", "+", "-"] * n
    num_list = list(i for i in range(1, n + 1))
    new_list = list(zip(num_list[::-1], symbols))
    # print(new_list)
    my_list = []
    for el in new_list:
        my_list.append(el[0])
        my_list.append(el[1])

    counter = 1
    result = 0
    if n in (1, 2): return n
    for i in range(len(my_list) - 1):
        if my_list[i] == "*" and counter == 1:
            if (i + 1) < len(my_list) and (i + 2) < len(my_list):
                result = my_list[i - 1] * my_list[i + 1] // my_list[i + 3]
            elif (i + 1) < len(my_list) and (i + 2) >= len(my_list):
                result = my_list[i - 1] * my_list[i + 1]

            counter += 1
        if my_list[i] == "*" and counter > 2:
            if (i + 1) < len(my_list) and (i + 3) < len(my_list):
                result -= my_list[i - 1] * my_list[i + 1] // my_list[i + 3]
            elif (i + 1) < len(my_list) and (i + 3) >= len(my_list):
                result -= my_list[i - 1] * my_list[i + 1]
            counter += 1
        if my_list[i] == "+":
            result += my_list[i + 1]
            counter += 1
    return result


for i in range(100):
    print(almoust_factorial(i))