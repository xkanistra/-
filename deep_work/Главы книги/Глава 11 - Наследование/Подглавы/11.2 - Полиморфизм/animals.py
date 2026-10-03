# Класса Mammal представляет род млекопитающих


class Mammal:
    # Метод принимает аргумент для
    # вида млекопитающего
    def __init__(self, special):
        self.__special = special

    # Метод показывает сообщение
    # о виде млекопитающего
    def show_special(self):
        print(f"Я - {self.__special}")

    # Метод издает звук характерный для
    # млекопитающего
    def make_sound(self):
        print("Гррррр")


# Класс Dog является подклассом класса Mammal


class Dog(Mammal):
    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'собака' в качестве вида.
    def __init__(self):
        Mammal.__init__(self, "собака")

    # Метод make_sound переопределяет метод
    # make_sound надкласса.
    def make_sound(self):
        print("Гав-гав!")


# Класс Cat является подклассом класса Mammal


class Cat(Mammal):
    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'кот' в качестве вида.
    def __init__(self):
        Mammal.__init__(self, "кот")

    # Метод make_sound переопределяет метод
    # make_sound надкласса.
    def make_sound(self):
        print("Мяу!")
