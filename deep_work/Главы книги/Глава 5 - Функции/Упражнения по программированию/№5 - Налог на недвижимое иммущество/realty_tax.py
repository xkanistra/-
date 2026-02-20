# Программа расчитывает показывает оценочную стоимость и налог на иммущество

# Налог на недвижимость в 60%
TAX = 0.6

# Налог в 72 цента на каждые 100$ оценочной стоимость
TAX_REALTY = 0.72


def main():
    realty = float(input("Введите стоимость недвижимости: "))
    appraised_value = get_appraised_value(realty)
    appraised_tax = get_appraised_tax(appraised_value)
    print(
        f"Оценочная стоимость: {appraised_value:.2f}%\n"
        f"Налог на иммущество: {appraised_tax:.2f}$"
    )


# Расчет оценочной стоимости
def get_appraised_value(realty):
    total_value = realty * TAX
    return total_value


# Расчет налога на иммущество
def get_appraised_tax(appraised_value):
    tax = (appraised_value / 100) * TAX_REALTY
    return tax

main()
