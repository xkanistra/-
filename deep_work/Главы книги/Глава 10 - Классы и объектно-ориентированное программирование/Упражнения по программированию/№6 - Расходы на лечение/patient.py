# Класс Patient

class Patient:
    def __init__(self, full_name, full_adress, mobile_number, emergency_contact):
        self.__full_name = full_name
        self.__full_adress = full_adress
        self.__mobile_number = mobile_number
        self.__emergency_contact = emergency_contact

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_full_adress(self, full_adress):
        self.__full_adress = full_adress

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    def __str__(self):
        return f'ФИО: {self.__full_name}\nПолный адресс: {self.__full_adress}\nТелефонный номер: {self.__mobile_number}\nКонтакты доверенного лица: {self.__emergency_contact}\n'

    def inf_list(self):
        information_list = []
        information_list.append(self.__full_name)
        information_list.append(self.__full_adress)
        information_list.append(self.__mobile_number)
        information_list.append(self.__emergency_contact)
        return ', '.join(information_list)