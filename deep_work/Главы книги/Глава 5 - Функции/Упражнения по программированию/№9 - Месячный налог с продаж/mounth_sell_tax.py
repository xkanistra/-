# Программа рассчитывает сумму, муниципального, федерального и общий налог с продаж.

# Константы налогов
FED_TAX = 0.05
MUNICIPAL_TAX = 0.025

def main():
    sell = float(input('Введите общий объем продаж: '))
    fed_tax = get_fed_tax(sell)
    municipal_tax = get_municipal_tax(sell)
    sum_tax = get_sum_tax(fed_tax, municipal_tax)
    print(f'Федеральный налог: {fed_tax:,.2f}$\n'
    f'Муниципальный налог: {municipal_tax:,.2f}$\n'
    f'Общий налог: {sum_tax:,.2f}$')
    
def get_fed_tax(sell):
    return sell * FED_TAX
    
    
def get_municipal_tax(sell):
    return sell * MUNICIPAL_TAX
    
    
def get_sum_tax(fed_tax, municipal_tax):
    return fed_tax + municipal_tax
    
main()