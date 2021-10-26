from abc import ABC, abstractmethod


class Close(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cloth(self):
        pass



# пальто
class Coat(Close):

    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 42:
            self.__size = 42
        elif size > 56:
            self.__size = 56
        else:
            self.__size = size

    def get_cloth(self):
        return round(self.__size / 6.5 + 0.5, 2)


# костюм
class Suit(Close):

    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            self.__height = 100
        elif height > 230:
            self.__height = 230
        else:
            self.__height = height

    def get_cloth(self):
        return round(self.__height * 2 + 0.3, 2)


my_coat = Coat('пальто', 42)
print(my_coat.size)

my_coat.size = 58
print(my_coat.size)
print(my_coat.get_cloth())

my_suit = Suit('синий костюм', 158)
print(my_suit.height)

my_suit.height = 235
print(my_suit.height)
print(my_suit.get_cloth())
