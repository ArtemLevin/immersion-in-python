# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def func_1():
    flag = True
    while flag:
        number_to_guess = int(input("Number to guess: "))
        print("Number is not in correct interval. Enter the correct number") if number_to_guess not in (
            range(0, 101)) else flag = False
    attempts_to_guess = int(input("Attempts to guess: "))

    def guessTheNumber():
        nonlocal number_to_guess, attempts_to_guess
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

    return func_2


guess_machine = func_1()
attempts = guess_machine()
