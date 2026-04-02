# Конвертер валют

# Модуль для работы с датой и временем
import datetime
# Модуль для чтения файлов больших
from collections import deque


DOLLAR = 2.93           # Стоимость одного доллара в BYN
EURO = 3.4              #Стоимость одного евро в BYN

def main():
    found = 'д'
    while found == 'д' or found == 'Д':
        choise = main_menu()   
        if choise == 1:
            date = datetime.datetime.now()
            amount = get_amount()
            currency_choice = get_currency_choice(DOLLAR, EURO)
            convert_result = convert(amount, currency_choice)
            print_report(currency_choice, DOLLAR, EURO, convert_result)
            save_transaction(amount, currency_choice, convert_result, date, DOLLAR, EURO)
            found = input('Желаете продолжить? Введите д/Д если да, остальное завершит программу: ')   

        elif choise == 2:   
            show_last_5()
            found = input('Желаете продолжить? Введите д/Д если да, остальное завершит программу: ')
            
        else:
            print("Программа законченна")
            break

# Функция создающая меню.
def main_menu():
    print("=" * 3, "Конвентер валют", "=" * 3)
    print(f"1. Конвентировать")
    print(f"2. История операций")
    print(f"3. Выход")
    choise = int(input("Выберите действие: "))
    while choise < 1 or choise > 3:
        print("ОШИБКА. Не допустимое значение")
        choise = int(input("Введите допустимое значение(1, 2 или 3): "))
    return choise

# Функция запрашивает сумму для конвертации
def get_amount():
    amount = float(input('Введите сумму (BYN): '))
    while amount < 0:
        amount = float(input('!' * 3, 'ОШИБКА', '!' * 3,'\n','Не допустимая сумма, введите корректную сумму(> 0): '))
    return amount

# Выбор нужной валюты
def get_currency_choice(DOLLAR, EURO):
    print(f"1 - USD, 2 - EUR")
    currency = int(input('Выберите нужную валюту: '))
    while currency < 1 or currency > 2:
        currency = int(input('ОШИБКА! Выберите нужную валюту: '))
    if currency == 1:
        return DOLLAR
    else:
        return EURO

def convert(amount, currency_choice):
    total = amount / currency_choice
    return total

# Функция для вывода результата
def print_report(currency_choice, DOLLAR, EURO, convert_result):
    if currency_choice == DOLLAR:
        print(f'Результат: {convert_result:.2f} USD')
    elif currency_choice == EURO:
        print(f'Результат: {convert_result:.2f} EUR')

# Функция сохраняющая данные в файл
def save_transaction(amount, currency_choice, convert_result, date, DOLLAR, EURO):
    with open(r'Project/Pet_project/Конвентер валют с историей/conversion_history.txt', 'a', encoding = 'utf-8') as convertFile:
        if currency_choice == DOLLAR:
            convertFile.write(f'{date} | {amount} BYN -> {convert_result:.2f} USD\n')
        elif currency_choice == EURO:
            convertFile.write(f'{date} | {amount} BYN -> {convert_result:.2f} EUR\n')
    print("✅️Записано в conversion_history.txt")

# Показать последние 5 записей
def show_last_5():
    with open(r'Project/Pet_project/Конвентер валют с историей/conversion_history.txt', 'r', encoding = 'utf-8') as convertFile:
        last_5_lines = deque(convertFile, maxlen=5)
        for line in last_5_lines:
            print(line.rstrip())

if __name__ == '__main__':
    main()

