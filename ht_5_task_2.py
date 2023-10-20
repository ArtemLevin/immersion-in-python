names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

bonus_dict = {i[0]: i[1] * int(i[2][: - 1]) / 100
for i in list(zip(names, salary, bonus))}
print(bonus_dict)

