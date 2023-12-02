# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from seminar_tasks.seminar_10.s_10_t_3 import Person


class Employee(Person):
    def __init__(self, id, *args):
        self.id = id
        super().__init__(*args)

    def get_access_id(self):
        return sum([int(x) for x in str(self.id)]) % 7


Den = Employee(864192, "Den", "Kek", 29)

print((f"{Den.get_access_id() = }"))
print((f"{Den.get_age() = }"))
