# Программа создает экземляр класса SavingsAccount
# и экземпляр CD

import accounts


def main():

    print("Введите данные о сберегательном счета.")
    acct_num = input("Номер счета: ")
    int_rate = float(input("Процентная ставка: "))
    balance = float(input("Остаток: "))

    savings = accounts.SavingsAccount(acct_num, int_rate, balance)

    print("Введите данные о счете CD.")
    acct_num = input("Номер счета: ")
    int_rate = float(input("Процентная ставка: "))
    balance = float(input("Остаток: "))
    maturity = input("Дата погашения: ")

    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    print("Вот введенные Вами данные:")
    print()
    print("Сберегательный счет")
    print("-------------------")
    print(f"Номер счета: {savings.get_account_num()}")
    print(f"Процетная ставка: {savings.get_int_rate()}")
    print(f"Остаток: ${savings.get_bal()}")
    print()
    print("Счет депозитного сертификата (CD)")
    print("---------------------------------")
    print(f"Номер счета: {cd.get_account_num()}")
    print(f"Процетная ставка: {cd.get_int_rate()}")
    print(f"Остаток: ${cd.get_bal()}")
    print(f"Дата погашения: {cd.get_maturity_date()}")


if __name__ == "__main__":
    main()
