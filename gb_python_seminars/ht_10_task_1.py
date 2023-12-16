class Animal():
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, wing_span, name):
        self.wing_span = wing_span
        super().__init__(name)

    def wing_length(self):
        return self.wing_span


class Fish(Animal):
    def __init__(self, max_depth, name):
        self.max_depth = max_depth
        super().__init__(name)

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, weight, name):
        self.weight = weight
        super().__init__(name)

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory():
    @classmethod
    def create_animal(self, animal_type, *args):
        if animal_type == "Bird":
            return Bird(args[1], args[0])

        elif animal_type == "Fish":
            return Fish(args[1], args[0])

        elif animal_type == "Mammal":
            return Mammal(args[1], args[0])


animal2 = AnimalFactory.create_animal('Fish', 'Salmon', 50)
print(animal2.depth())
