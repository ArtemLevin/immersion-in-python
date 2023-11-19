# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from random import randint


def valueControl(myFunc):
    def wrapper(*args):
        number_to_guess = int(input("Number to guess: "))
        if number_to_guess not in (range(0, 101)):
            number_to_guess =  randint(1, 101)
            print(f"Number to guess: {number_to_guess}")
        attempts_to_guess = int(input("Attempts to guess: "))
        if attempts_to_guess not in (range(0, 11)):
            attempts_to_guess = randint(1, 11)
            print(f"Attempts to guess: {attempts_to_guess}")
        return myFunc(number_to_guess, attempts_to_guess)

    return wrapper


@valueControl
def func_2(number_to_guess, attempts_to_guess):
    counter = -1
    while True:
        counter += 1
        if counter == attempts_to_guess:
            return print("Attempts ended")
        your_attempt = int(input("Enter your number: "))
        if your_attempt == number_to_guess:
            return print("You guessed right!")
        else:
            print("You guessed wrong")

func_2()