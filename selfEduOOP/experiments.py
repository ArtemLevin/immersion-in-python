import random

actionList = ["+", "-", "*"]
i = 1
while i < 31:
    with open("action.doc", "a", encoding="utf-8") as file:
        file.write(f"{i}) ({random.randint(-50, 50):+}){random.choice(actionList)}({random.randint(1, 50):+}) = \n")
    i+=1

