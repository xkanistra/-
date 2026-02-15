# Конвертер значение между единицами по выбору.
# Главная функция программы.
def main():
    main_menu()
    input_selection()

# Функция создающая меню.
def main_menu():
    print("~" * 3, "МЕНЮ", "~" * 3)
    print("1. Температура")
    print("2. Длинна")

# Функция выбора действия.
def input_selection():
    selection = int(input("Выберите необходимую единицу для конвертации: "))
    
    if selection == 1:
        print("a. C -> F")
        print("b. F -> C")
        select = input("Выберите единицу измерения: ")
        if select == "a" or select == "A":
            c = float(input("Введите кол-во градусов C для перевода: "))
            f = (c * (9 / 5)) + 32
            print("Градусы C\tГрадусы F")
            print(f"{c:.1f}\t\t{f:.1f}")
        elif select == "b" or select == "B":
            f = float(input("Введите кол-во градусов f для перевода: "))
            c = (f - 32) * (5 / 9)
            print("Градусы F\tГрадусы C")
            print(f"{f:.1f}\t\t{c:.1f}")
        else:
            print("ОШИБКА! Неверный тип конвертации")

    elif selection == 2:
        print("a. см -> м")
        print("a. м -> см")
        select = input("Выберите единицу измерения: ")
        if select == "a" or select == "A":
            cm = float(input("Введите кол-во см для перевода: "))
            m = cm / 100
            print("Сантиметры\tМетры")
            print(f"{cm:.2f} см\t{m:.2f} м")
        elif select == "b" or select == "B":
            m = float(input("Введите кол-во м для перевода: "))
            cm = m * 100
            print("Метры\tСантиметры")
            print(f"{m:.2f} м\t{cm:.2f} см")
        else:
            print("ОШИБКА! Неверный тип конвертации")

    else:
        print("ОШИБКА! Неверный тип конвертации")

main()

