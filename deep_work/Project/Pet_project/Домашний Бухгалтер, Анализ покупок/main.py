# 'Ядро' работы программы
#from menu import main_menu
from pathlib import Path
DATA_FILE = 'Project/Pet_project/Домашний Бухгалтер, Анализ покупок/Список/Список.txt'

def main():
    create_file(DATA_FILE)
    main_menu()
    choices = int(input())
    if choices == 1:
        again = 'д'
        while again == 'д' or again == 'Д':
            products_name, cost, amount = get_product_info()
            product_list = add_to_list(products_name, cost, amount)
            save_file(product_list, DATA_FILE)
            again = input(f'Желаете добавить еще продукт? Д/д - да: ')
            if again == 'д' or again == 'Д':
                again = 'д'
            else:
                break
def main_menu():
    print(f'Выберите необходимое действие:\n'
          f'1. Добавить товар\n'
          f'2. Показать текущий список\n'
          f'3. Сохранить и выйти')
    
def get_product_info():
    again = 'д'
    while again == 'д' or again == 'Д':
        products_name = input('Введите название: ')
        cost = float(input('Введите цену: '))
        amount = int(input('Введите количество: '))
        print(f'Товар добавлен!')
        return products_name, cost, amount
        
def add_to_list(product, cost, amount):
    product_list = []
    product_list.append(product)
    product_list.append(cost)
    product_list.append(amount)

def create_file(DATA_FILE):
    shoping_tuple = ('Название товара', 'Цена', 'Количество')

    if not Path(DATA_FILE).exists():
        print(f'Файл не найден, создаем новый файл.')
        with open(DATA_FILE, 'a', encoding='utf-8') as createFile:
            createFile.write(f'{shoping_tuple}\n')
    
def save_file(product_list, DATA_FILE):    
    with open(DATA_FILE, 'a', encoding='utf-8') as saveFile:
        saveFile.write(f'{product_list}\n')


if __name__ == '__main__':
    main()