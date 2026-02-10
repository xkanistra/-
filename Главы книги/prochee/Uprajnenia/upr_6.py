shop = float(input("Введите величину покупки "))
FED_TAX = 0.05
REG_TAX = 0.025
fed = shop * FED_TAX
reg = shop * REG_TAX
sum_tax = fed + reg
sum = sum_tax + shop
print(
    f"Величина покупки равняется {shop:.2f} рублей\n"
    f"Федеральный налог равняется {fed:.2f} рублей\n"
    f"Региональный налог равняется {reg:.2f} рублей\n"
    f"Общий налог равняется {sum_tax:.2f} рублей\n"
    f"Общая сумма покупки равняется {sum:.2f} рубелей"
)
