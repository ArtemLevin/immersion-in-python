class PhoneNumber:
    def __init__(self,number, fio):
        if type(number) is int and len(list(number)) == 1:
            self.number = number
        else:
            raise ValueError("Invalid phone number")
        if type(fio) == str:
            self.fio = fio
        else:
            raise ValueError("Invalid fio")

class PhoneBook:
    def __init__(self):
        self.phoneList = []

    def add_phone(self, phone):
        self.phoneList.append(phone)

    def remove_phone(self, idx):
        self.phoneList.pop(idx)

    def get_phone_list(self):
        return self.phoneList


