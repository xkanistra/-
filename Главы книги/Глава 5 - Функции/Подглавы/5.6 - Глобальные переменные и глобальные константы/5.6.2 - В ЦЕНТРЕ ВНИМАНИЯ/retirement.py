# Программа демонстрирует исп. глобальной константы
# для предоставления ставки взноса 
CONRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Введите ЗП: '))
    bonus = float(input('Введите премию: '))
    show_pay_conrib(gross_pay)
    show_bonus_conrib(bonus)

# Функция show_pay_conrib принимает аргументом
# ЗП(gross_pay) сотрудника и показывает взнос
# в пенсионные накопления исходя из размера ЗП 
def show_pay_conrib(gross):
    contrib = gross * CONRIBUTION_RATE
    print(f'Взнос исходя из ЗП: {contrib:,.2f}$')

# Функция show_bonus_conrib принимает аргументом
# премию(bonus) сотрудника и показывает взнос
# в пенсионные накопления исходя из размера премии 
def show_bonus_conrib(bonus):
    contrib = bonus * CONRIBUTION_RATE
    print(f'Взнос исходя из премий: {contrib:,.2f}$')

main()