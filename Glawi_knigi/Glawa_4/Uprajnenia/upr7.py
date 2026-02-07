# Мелкая монета для зарплаты.

day = int(input('Введите количество отработанных дней: '))

print('Дни \t Доход')
print('-' * 20)

total = 0.0

for d in range(1 , day + 1):
    income = 2 ** (d - 1)
    total += income
    print(f'{d:.0f} \t {income:.2f}')

total_rub = total / 100
print(f'ЗП за {day} дней соствляет {total_rub:.2f} р')