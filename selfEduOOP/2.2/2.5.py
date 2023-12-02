class WindowDlg():
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = self.__height = None
        self.height = height
        self.width = width

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == str and 0 <= value <= 10 ** 4:
            if self.__width: self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == str and 0 <= value <= 10 ** 4:
            if self.__width: self.show()
            self.__height = value

