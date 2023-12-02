# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive():

    """ Archive class """
    list_str = []
    list_num = []

    def __init__(self, mystring: str, mynum: int):
        self.mystring = mystring
        self.mynum = mynum
        self.list_str.append(self.mystring)
        self.list_num.append(self.mynum)


obj_1 = Archive("hello world", 1)
print(obj_1.list_num, obj_1.list_str)
obj_2 = Archive("hello everyone", 2)
print(obj_2.list_num, obj_2.list_str)


