import itertools
import random

def generate_boards():
    def check_queens(queens):
        for el in list(itertools.combinations(queens, 2)):
            if el[0][0] == el[1][0] or el[0][1] == el[1][1] or abs(el[0][0] - el[1][0]) == abs(el[0][1] - el[1][1]):
                return False
        return True


    counter = 1
    board_list = []
    while counter < 5:
        pos = [(random.randint(1, 9), random.randint(1, 9)) for _ in range(1, 9)]
        # print(pos)
        if check_queens(pos):
            board_list.append(pos)
            counter += 1

    return board_list

print(generate_boards())
