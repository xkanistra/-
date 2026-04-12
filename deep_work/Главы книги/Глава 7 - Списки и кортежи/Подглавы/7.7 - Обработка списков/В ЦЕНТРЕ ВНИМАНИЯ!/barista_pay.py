# Программа вычисляет ЗП
# каждого работника 

# Константа для размера списка
NUM_EMPLOYEES = 6

def main():
    # Создать список содержащий кол-во отработанных часов
    hours = [0] * NUM_EMPLOYEES

    # Получить часы отработанные каждым сотрудником
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Введите число отработанных часов сотрудником {index + 1}: '))

    # Получить почасовую ставку
    pay_rate = float(input(f'Введите почасовую ставку оплаты: '))

    # Показать ЗП каждого сотрудника
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'ЗП сотрудника {index + 1}: {gross_pay:.2f}$')

if __name__ == '__main__':
    main()