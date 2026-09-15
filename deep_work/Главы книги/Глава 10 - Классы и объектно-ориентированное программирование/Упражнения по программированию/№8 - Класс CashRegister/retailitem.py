# Класс RetailItem

class RetailItem:
    def __init__(self, description, quantity, price):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description 
    
    def get_quantity(self):
        return self.__quantity
    
    def get_price(self):
        return self.__price 

    def __str__(self):
        return f'Описание: {self.__description}\nКоличество на складе: {self.__quantity}\nЦена: {self.__price:,.2f}\n'

    def inf_list(self):
        information_list = []
        information_list.append(self.__description)
        information_list.append(self.__quantity)
        information_list.append(self.__price)
        return information_list
