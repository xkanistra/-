# Программа выводит статистику дождевых осадков

MOUNTHS = 12


def main():
    total_rainfall = 0.0
    rainfall_list = []
    for mounth in range(1, MOUNTHS + 1):
        rainfall = float(input(f"Введите значение дождевых осадков за {mounth} месяц: "))
        rainfall_list.append(rainfall)

    for item in rainfall_list:
        total_rainfall += float(item)
        average_rainfall = total_rainfall / MOUNTHS
    
    min_rainfall = min(rainfall_list)
    max_rainfall = max(rainfall_list)
    min_idex = rainfall_list.index(min_rainfall)
    max_index = rainfall_list.index(max_rainfall)
    
    print(rainfall_list)
    print(f"Общее кол-во осадков за год: {total_rainfall:.2f} мм\n"
        f"Среднее кол-во осадков за год: {average_rainfall:.2f} мм\n"
        f"Минимальное кол-во осадков в {min_idex + 1} месяце: {min_rainfall:.2f} мм\n"
        f"Максимальное кол-во осадков в {max_index + 1} месяце: {max_rainfall:.2f} мм")


if __name__ == "__main__":
    main()
