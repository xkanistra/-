# Программа расчитывает кол-во потребляемых калорий из жиров и углеводов

# Константы
# Калория на 1 гр жира
FAT_CAL = 9

# Калория на 1 гр углеводов
CARB_CAL = 4


def main():
    amount_fat = int(input("Введите сколько грамм жиров употребили: "))
    amount_carb = int(input("Введите сколько грамм углеводов употребили: "))
    fat_cal = get_fat_cal(amount_fat)
    carb_cal = get_carb_cal(amount_carb)
    total_cal = get_total_cal(fat_cal, carb_cal)
    print(
        f"Калорий из жиров: {fat_cal}\n"
        f"Калорий из углеводов: {carb_cal}\n"
        f"Общее кол-во калорий из жиров и углеводов: {total_cal}"
    )


# Расчет кол-ва калорий из жиров
def get_fat_cal(amount_fat):
    result = amount_fat * FAT_CAL
    return result


# Расчет кол-ва калорий из углеводов
def get_carb_cal(amount_carb):
    result = amount_carb * FAT_CAL
    return result


def get_total_cal(fat_cal, carb_cal):
    total = fat_cal + carb_cal
    return total

main()
