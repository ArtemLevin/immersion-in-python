class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None :
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:

    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj

        if self.top is None:
            self.top = obj

    def pop(self):
        current_obj = self.top
        if current_obj is None: return
        while current_obj and current_obj.next != self.last:
            current_obj = current_obj.next
        if current_obj:
            current_obj.next = None
        last = self.last
        self.last = current_obj
        if self.last is None:
            self.top = None
        return last


    def get_data(self):
        obj = self.top
        dataList = []
        while obj:
            dataList.append(obj.data)
            obj = obj.next
        return dataList

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.pop().data)

res = st.get_data()  # ['obj1', 'obj2']
print(res)