class SuperShop:
    goods =[]

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_product(cls, product):
        cls.goods.append(product)

    @classmethod
    def remove_product(cls, product):
        cls.goods.remove(product)


class StringValue:

    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self._name, value)


class PriceValue:

    def __init__(self,  max_value=10**4):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= len(str(value)) <= self.max_value:
            setattr(instance, self._name, value)

class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")