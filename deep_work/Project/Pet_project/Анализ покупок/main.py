# Программа по учету и анализу покупок
DATA_FILE = "Project/Pet_project/Анализ покупок/Список/Список.txt"
MOUNTH_BUDGET = int(input('Введите ваш месячный бюджет: '))

def main():
    choice = main_menu()
    if choice == 1:
        total = 0
        again = 'д'
        while again == 'Д' or again == 'д':
            total += 1
            name, cost, amount = add_products(total)
            products_list = add_list(name, cost, amount)
            save_file(products_list, DATA_FILE)
            again = input('Желаете добавить еще товар? Д/д - Да: ')
            if again == 'Д' or again == 'д':
                again = 'д'
                print()
            else:
                print()
                break
        

def main_menu():
    print(f"Выберите действие:\n" 
          f"1.Добавить товар")
    choice = int(input())
    print()
    return choice


def add_products(total):
    name = input(f"Введите товар {total}: ")
    cost = float(input("Введите стоимость: "))
    amount = int(input("Введите количество: "))
    return name, cost, amount


def add_list(name, cost, amount):
    products_list = [name, cost, amount]
    return products_list


def save_file(products_list, DATA_FILE):
    with open(DATA_FILE, "a", encoding="utf-8") as saveFile:
        products =', '.join(map(str, products_list))
        saveFile.write(f'{products}\n')
        print(f"Данные сохранены в файл!")


if __name__ == "__main__":
    main()
