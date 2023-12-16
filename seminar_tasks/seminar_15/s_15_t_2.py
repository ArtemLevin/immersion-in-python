# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


import logging
from functools import wraps

logging.basicConfig(
                    filename='logs/logs.log',
                    format="{filename} - {asctime} - {msg}",
                    style="{",
                    level=logging.INFO)
logger = logging.getLogger("app")

def log_func(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"Function {func.__name__} has been successfully decorated")
                return result
            except Exception as e:
                logger.exception(f"Exception {e}")
                raise
        return wrapper

    return decorator



if __name__ == "__main__":
    @log_func(logger)
    def divisionBy():
        a = int(input("enter a: "))
        b = int(input("enter b: "))
        try:
            return a/b
        except ZeroDivisionError as e:
            logger.error(f"Error {e} --------- b can't be 0")


    divisionBy()
