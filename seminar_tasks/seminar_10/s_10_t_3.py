class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def increment_age(self):
        self.__age += 1

    def get_age(self):
        return self.__age
#
# Den = Person("Den", "Kek", 20)
#
# print(f"{Den.get_age() = }")
#
# Den.increment_age()
#
# print(f"{Den.get_age() = }")

