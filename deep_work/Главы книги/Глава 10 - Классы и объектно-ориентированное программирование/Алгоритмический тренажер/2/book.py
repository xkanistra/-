# Класс Book

class Book:
    def __init__(self, headline, name, publisher):
        self.__headline = headline
        self.__name = name
        self.__publisher = publisher

    def __str__(self):
        return f'Заголовок: {self.__headline}\nИмя: {self.__name}\nИздатель: {self.__publisher}'
        