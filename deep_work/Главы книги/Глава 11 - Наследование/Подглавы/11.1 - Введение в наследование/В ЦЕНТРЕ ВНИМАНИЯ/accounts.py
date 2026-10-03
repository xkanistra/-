# Класс SavingsAccount представляет
# сберегательный счет.


class SavingsAccount:
    # Инициализируем атрибуты класса, принимающенго
    # номер счета, процентной ставки и баланс
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__int_rate = int_rate
        self.__balance = bal

    # Ниже методы-мутаторы атрибутов данных
    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_int_rate(self, int_rate):
        self.__int_rate = int_rate

    def set_bal(self, bal):
        self.__balance = bal

    # Методы-получатели атрибутов данных
    def get_account_num(self):
        return self.__account_num

    def get_int_rate(self):
        return self.__int_rate

    def get_bal(self):
        return self.__balance


# Класс CD представляет счет
# депозитного сертификата(CD).
# Это подкласс класса SavingsAccount


class CD(SavingsAccount):
    # Инициализируем аргументы для номера счета, процентной ставки,
    # баланса и даты погашения
    def __init__(self, account_num, int_rate, bal, mat_date):
        # Вызвать метод init надкласса SavingsAccount
        SavingsAccount.__init__(self, account_num, int_rate, bal)
        # Инициализировать атрибут __maturity_date
        self.__maturity_date = mat_date

    # Метод set_maturity_date является методом-мутатором
    # атрибута __maturity_date
    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # Метод get_maturity_date является методом-получателем
    # атрибута __maturity_date
    def get_maturity_date(self):
        return self.__maturity_date
