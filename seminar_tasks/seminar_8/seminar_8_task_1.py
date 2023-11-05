# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json
import os

FILE_NAME = "users.json"

def user_id_by_access_level():
    if f'{FILE_NAME}' not in os.listdir(os.getcwd()):
        users_dict = {}
        with open(f'{FILE_NAME}', "w") as f:
            json.dump(users_dict, f)
    with open(f'{FILE_NAME}', "r") as f:
        users_dict = json.load(f)
    with open(f'{FILE_NAME}', "w") as f:
        flag = True
        while flag:
            user_id = int(input("Enter your id: "))
            flag = True
            while flag:
                if user_id not in users_dict.keys():
                    name = input("Enter your name: ")
                    user_id_name = {f'user_id_{user_id}': name}
                    flag = False
                else:
                    user_id = int(input("Enter your correct id: "))
            flag = True
            while flag:
                access_level = int(input("Enter your access level: "))
                if access_level in (range(1, 8)):
                    if f'access_level_{access_level}' not in users_dict.keys():
                        users_dict[f'access_level_{access_level}'] = []
                        users_dict[f'access_level_{access_level}'].append(user_id_name)
                        flag = False
                    else:
                        users_dict[f'access_level_{access_level}'].append(user_id_name)
                        flag = False
                else:
                    print("enter your correct access level")
            flag = True if input("Would you like to continue? Press 'y' to continue or any other to escape: ") == "y" else False
        json.dump(users_dict, f)


if __name__ == "__main__":
    user_id_by_access_level()
