# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging
logging.basicConfig(
    filename='logs/errors.log',
    encoding="utf-8",
    format='{levelname} - {asctime} - {msg}',
    style="{",
    level=logging.INFO)
logger = logging.getLogger("app")

def divisionBy():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    try:
        return a/b
    except ZeroDivisionError as e:
        logger.error(f"Error {e} \nb can't be 0")


if __name__ == '__main__':
    divisionBy()
