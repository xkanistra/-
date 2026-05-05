# Программа расчитывает общую сумму продаж и сохр её в список
DAYS = 7
DATA_LIST = "Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Решение для задач/Доходы за неделю.txt"


def main():
    values = calculate_total()
    save_file = save_list_to_file(values)
    print(f'Доход за неделю составил: {values} руб')


def calculate_total():
    total_value = 0.0
    for day in range(1, DAYS + 1):
        values = float(input(f'Введите доход за день {day}: '))
        total_value += values
    return total_value


def save_list_to_file(values):
    values_list = [values]
    with open(DATA_LIST, "a", encoding="utf-8") as saveFile:
        for item in values_list:
            saveFile.write(f"{item}\n")
    return values_list


if __name__ == "__main__":
    main()
