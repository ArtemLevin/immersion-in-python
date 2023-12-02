# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time


class MyString(str):
    def __new__(cls, author: str, text: str):
        instance = super().__new__(cls, text)
        instance.author = author
        instance.text = text
        instance.creationTime = time.strftime("%Y-%m-%d %H:%M")
        return instance


print(MyString('ben', "text"))
