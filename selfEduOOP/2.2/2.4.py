class Car:
    def __init__(self):
        self.__model = None


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and len(model) in range(2,101):
            self.__model = model
