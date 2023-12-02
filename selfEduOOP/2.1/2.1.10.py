import random
import string


class EmailValidator:
    def __new__(cls):
        if super().__new__(cls):
            return print(None)

    @classmethod
    def get_random_email(cls):
        pwd = ''
        symList = list(string.ascii_lowercase) + [str(i) for i in range(11)] + ["_", "."]
        for i in range(random.randint(0, 10)):
            pwd += random.choice(symList)
        pwd += '@gmail.com'
        return pwd

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email): return False
        symList = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_."

        if not set(email) < set(symList): return False

        s = email.split("@")
        if len(s) != 2: return False

        if len(s[0]) > 100 or len(s[1]) > 50: return False

        if "." not in s[1]: return False

        if email.count("..") > 0: return False

        return True

    @staticmethod
    def __is_email_str(email):

        return type(email) == str



print(EmailValidator.check_email("sc_lib@list.ru"))
print(EmailValidator.check_email("sc..lib@list_ru"))
