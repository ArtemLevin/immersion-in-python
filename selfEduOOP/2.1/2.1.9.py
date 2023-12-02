class LinkedList:
    def __init__(self):

        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if not self.tail:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next()

        self.tail = prev
        if not self.tail:
            self.head = None

    def get_data(self):
        dataList = []
        obj = self.head
        while obj:
            dataList.append(obj.get_data())
            obj = obj.get_next()

        return dataList


class ObjList:
    def __init__(self, data, next=None, prev=None):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def set_next(self, obj=None):
        self.__next = obj

    def set_prev(self, obj=None):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()