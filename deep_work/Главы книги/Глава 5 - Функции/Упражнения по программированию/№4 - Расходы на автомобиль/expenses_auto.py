# Программа расчитывает введенные пользователем обязательные платежи на авто.

YEAR = 12

def main():
    autocredit = autocredit_expenses()
    belay = belay_expenses()
    fuel = fuel_expenses()
    oil = oil_expenses()
    busbar = busbar_expenses()
    technical_service = technical_service_expenses()
    total_expenses = get_total_expenses(autocredit, belay, fuel, oil, busbar, technical_service)
    year_expenses = get_yaer_expenses(total_expenses)

    # Показать итоговые расходы
    print(f'Сумма месячных раходов составляет: {total_expenses:.2f}$')
    print(f'Сумма годовых раходов составляет: {year_expenses:.2f}$')

# Расходы на кредит
def autocredit_expenses():
    autocredit = float(input('Введите траты на автокредит: '))
    return autocredit

# Расходы на страховку
def belay_expenses():
    belay = float(input('Введите траты на страхование: '))
    return belay

# Расходы на бензин
def fuel_expenses():
    fuel = float(input('Введите траты на бензин: '))
    return fuel

# Расходы на масло
def oil_expenses():
    oil = float(input('Введите траты на масло: '))
    return oil

# Расходы на шины
def busbar_expenses():
    busbar = float(input('Введите траты на шины: '))
    return busbar

# Расходы на ТО
def technical_service_expenses():
    technical_service = float(input('Введите траты на ТО: '))
    return technical_service

# Расчет ежемесячных расходов 
def get_total_expenses(autocredit, belay, fuel, oil, busbar, technical_service):
    mounth_expenses = autocredit + belay + fuel + oil + busbar + technical_service
    return mounth_expenses

# Расчет годовых расходов
def get_yaer_expenses(total_expenses):
    return total_expenses * YEAR

main()