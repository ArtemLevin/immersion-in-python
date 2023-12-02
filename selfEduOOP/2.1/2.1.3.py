class Clock:
    def __init__(self, time):
        self.time = 0
        if self.__check_time(time):
            self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if type(tm) == int and (tm >= 0 and tm < 10 ** 4):
            return True


clock = Clock(4530)
