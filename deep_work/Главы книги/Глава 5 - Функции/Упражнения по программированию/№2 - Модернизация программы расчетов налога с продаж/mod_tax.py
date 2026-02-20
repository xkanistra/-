# Программа расчитывает налог с продаж

# Константы налогов
FED_TAX = 0.05
REG_TAX = 0.025

def main():
    shop = float(input("Введите величину покупки: "))
    fed_tax = get_fed_tax(shop)
    reg_tax = get_reg_tax(shop)
    total_tax = get_sum_tax(fed_tax, reg_tax)
    total_price = get_total_price(total_tax, shop)
    print(
        f"Величина покупки равняется {shop:.2f} рублей\n"
        f"Федеральный налог равняется {fed_tax:.2f} рублей\n"
        f"Региональный налог равняется {reg_tax:.2f} рублей\n"
        f"Общий налог равняется {total_tax:.2f} рублей\n"
        f"Общая сумма покупки равняется {total_price:.2f} рубелей"
    )

def get_fed_tax(shop):
    fed = shop * FED_TAX
    return fed

def get_reg_tax(shop):
    reg = shop * REG_TAX
    return reg

def get_sum_tax(fed, reg):
    sum_tax = fed + reg
    return sum_tax

def get_total_price(total_tax, shop):
    total_price = total_tax + shop
    return total_price

main()