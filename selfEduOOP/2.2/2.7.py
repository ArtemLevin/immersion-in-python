class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2
