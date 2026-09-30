# Класс Person


class Person:
    # Инициализация атрибутов
    def __init__(self, name, adress, mob_num):
        self.__name = name
        self.__adress = adress
        self.__mob_num = mob_num

    # Получить имя клиента
    def set_name(self, name):
        self.__name = name

    # Получить адрес клиента
    def set_adress(self, adress):
        self.__adress = adress

    # Получить мобильный номер
    def set_mob_num(self, mob_num):
        self.__mob_num = mob_num

    # Вернуть имя клиента
    def get_name(self):
        return self.__name

    # Вернуть адрес клиента
    def get_adress(self):
        return self.__adress

    # Вернуть мобильный номер
    def get_mob_num(self):
        return self.__mob_num


# Подкласс Customer
class Customer(Person):
    # Инициализация атрибутов
    def __init__(self, name, adress, mob_num, client_num, mailing):
        Person.__init__(self, name, adress, mob_num)
        self.__client_num = client_num
        self.__mailing = mailing

    # Получить номер клиента
    def set_client_num(self, client_num):
        self.__client_num = client_num

    # Получить согласие/несогласие на рассылку
    def set_mailing(self, mailing):
        self.__mailing = mailing

    # Вернуть номер клиента
    def get_client_num(self):
        return self.__client_num

    # Вернуть согласие/несогласие на рассылку
    def get_mailing(self):
        if self.__mailing == True:
            return f"согласен"
        else:
            return f"не согласен"
