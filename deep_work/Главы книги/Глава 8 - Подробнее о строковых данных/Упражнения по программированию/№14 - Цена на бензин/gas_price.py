# Программа вычисляет среднюю цену бензина за год
# Среднюю цену в каждом месяце
# Вычисляет самую высокую и самую низкую цену в месяце выводя дату
# Генерирует файл с датой и ценой от меньшей к большей
# Генерирует файл с датой и ценой от большей к меньшей


DATA_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/GasPrices.txt'

def main():
    gas_price = open_file()
    gas_list = add_list(gas_price)
    #avg_price_year = get_avg_price(gas_list)
def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        line = file.readlines()
    return line
    

def add_list(gas_price):
    gas_list = []
    new_gas_list = []
    for group in gas_price:
        new_group = group.rstrip('\n')
        split_group = new_group.split(':')  
        gas_list.append(split_group)
        for item in gas_list[0]:
            new_split_group = item.split('-')
            new_gas_list.append(new_split_group)

    print(new_gas_list)
    
        # Ниже код который решил пока не удалять, чтобы не забыть сам алгоритм
        #for item in split_group[:1]:
            #new_list = item.split('-')
            #gas_list.append(new_list[:])
            #gas_list.append(split_group[-1])


def get_avg_price(gas_list):
    price_counter = 0
    for group in gas_list:
        price_counter += float(group[-1])
    print(price_counter)
    
if __name__ == '__main__':
    main()