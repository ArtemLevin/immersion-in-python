class Shop:
    def __init__(self, goods):
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    attr_dict = {"id": (int,), "name": (str,), "weight": (int, float), "price": (int, float)}
    _id_instance = 1
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product._id_instance
        Product._id_instance +=1

    def __setattr__(self, key, value):
        if key in self.attr_dict.keys() and type(value) in self.attr_dict[key]:
            if (key=='price' or key=='weight') and value <=0:
                raise TypeError("Неверный тип присваиваемых данных")
        elif key in self.attr_dict:
                raise TypeError("Неверный тип присваиваемых данных")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено")
        else:
            object.__delattr__(self, item)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

print(book.id)