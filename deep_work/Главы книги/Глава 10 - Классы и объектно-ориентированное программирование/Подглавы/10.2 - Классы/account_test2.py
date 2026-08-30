# Программа демонстрирует работу класса BankAccount

import bankaccount2

def main():
    # Получить начальный остаток
    start_bal = float(input('Введите начальный остаток: '))

    # Создать объект BankAccount
    saving = bankaccount2.BankAccount(start_bal)

    # Внести на счет ЗП пользователя
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет...')
    saving.deposit(pay)

    # Показать остаток
    print(saving)

    # Получить сумму для снятия с банковского счета
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета...')
    saving.withdraw(cash)

    # Показать остаток
    print(saving)

if __name__ == '__main__':
    main()
    