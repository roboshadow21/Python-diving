class Animals:
    """Base class for all inherited animal classes, contained main information such as name or breed."""

    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age

    def get_full_info(self):
        return f'{self.name}, {self.breed}, {self.age} years old'


class Dog(Animals):

    def __init__(self, height: int, *args, **kwargs):
        self.height = height
        super().__init__(*args, **kwargs)

    def get_dog_size(self):
        """Method divides all dog into dog size"""
        if self.height > 50:
            return f'Dog {self.name}, breed - {self.breed} is big breed'
        elif 30 < self.height < 50:
            return f'Dog {self.name}, breed - {self.breed} is medium breed'
        else:
            return f'Dog {self.name}, breed - {self.breed} is small breed'

    def older(self):
        self.age += 1
        return self.age


class Bird(Animals):

    def __init__(self, *args, **kwargs):
        self.__wings_size: int = False
        super().__init__(*args, **kwargs)

    def can_fly(self):
        return f'{self.breed} {self.name} can fly' if self.__wings_size else f'{self.breed} {self.name} can\'t fly'

    @property
    def wings(self):
        return self.__wings_size

    @wings.setter
    def wings(self, wing_size):
        if wing_size >= 5:
            self.__wings_size = True


class Fish(Animals):

    def __init__(self, colour: str, *args, **kwargs):
        self.__colour = colour
        super().__init__(*args, **kwargs)

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, new_colour):
        self.__colour = new_colour


class Factory:

    def __init__(self, colour: str, name: str, breed: str, age: int):
        self.colour = colour
        self.name = name
        self.breed = breed
        self.age = age

    def create_object(self):
        return Fish(self.colour, self.name, self.breed, self.age)


if __name__ == '__main__':
    f = Factory('red', 'Fedya', 'salmon', 1)
    fish = f.create_object()
    print(fish.age)
    print(fish.get_full_info())
    print(fish.colour)
    fish.colour = 'green'
    print(fish.colour)
