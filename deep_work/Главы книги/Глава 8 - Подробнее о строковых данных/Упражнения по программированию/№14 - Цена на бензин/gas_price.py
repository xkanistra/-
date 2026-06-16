# Программа вычисляет среднюю цену бензина за год
# Среднюю цену в каждом месяце
# Вычисляет самую высокую и самую низкую цену в месяце выводя дату
# Генерирует файл с датой и ценой от меньшей к большей
# Генерирует файл с датой и ценой от большей к меньшей


DATA_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/GasPrices.txt'
ASCENDING_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Решение для задач/Список цен упорядоченный по возрастанию'
DESCENDING_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Решение для задач/Список цен упорядоченный по убыванию'

def main():
    gas_price = open_file()
    gas_list = add_list(gas_price)
    year_list = add_year_list(gas_list)
    avg_price_year = get_avg_price_year(gas_list, year_list)
    print()
    avg_price_month = get_avg_price_month(gas_list)
    print()
    max_and_min_price = get_max_min_price(gas_list, year_list)
    print()
    generate_max_and_min_sort_file(gas_list)

def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        line = file.readlines()
    return line
    

def add_list(gas_price):
    gas_list = []
    for group in gas_price:
        new_group = group.rstrip('\n')                      # Удаляем \n из элементов в списке
        split_group = new_group.split('-')                  # Разбиваем строку по разделителям справа налево, начинаем с -
        new_split = split_group[2].split(':')               # Берем список, в нем последний индекс где не разбита строка, разбиваем ее по :
        gas_list.append(split_group[:2] + new_split)        # Объединяем в один список одну часть где есть дата, которую разделяли по - и часть разделенную по :

    return gas_list


def add_year_list(gas_list):
    year_list = []
    for group in gas_list:
        year = group[2]                                         # Присваиваем год по индексу
        if year not in year_list:                               # Проверям, если нет в списке года, то добавляем его, это уберет дубликаты
            year_list.append(year)  
    return year_list


def get_avg_price_year(gas_list, year_list):
    print('-' * 5, 'СРЕДНЯЯ ЦЕНА ЗА КАЖДЫЙ ГОД', '-' * 5)
    for year in year_list:                                      # Читаем циклом каждый год в списке
        total_price = 0                                         # Накопитель для цены, идет в цикле чтобы при каждой иттерации сбрасывался
        count = 0                                               # Накопитель для количества, идет в цикле чтобы при каждой иттерации сбрасывался

        for group in gas_list:
            if group[2] == year:                                # Условие, если год из первоначального списка есть в новом без дубликатов, то
                total_price += float(group[3])                  # Прибавляем накопителю цену
                count += 1                                      # Прибавляем накопителю количество

        avg_price = total_price / count                         # Расчет средней цены
        print(f'Год: {year}, Средняя цена: {avg_price:.3f}$')
        

# Такая же логика что и для года
def get_avg_price_month(gas_list):
    mounth_list = []
    print('-' * 5, 'СРЕДНЯЯ ЦЕНА ЗА КАЖДЫЙ МЕСЯЦ', '-' * 5)
    for group in gas_list:
        mounth = group[0]
        if mounth not in mounth_list:       
            mounth_list.append(mounth)      
    mounth_list.sort()
    
    for mounth in mounth_list:                                     
        total_price = 0                                        
        count = 0                                               

        for group in gas_list:
            if group[0] == mounth:                                
                total_price += float(group[3])                  
                count += 1                                      

        avg_price = total_price / count                         
        print(f'Месяц: {mounth}, Средняя цена: {avg_price:.3f}$')


def get_max_min_price(gas_list, year_list):
    print('-' * 5, 'НАИБОЛЬШАЯ И НАИМЕНЬШАЯ ЦЕНА ЗА КАЖДЫЙ ГОД', '-' * 5)
    for year in year_list:
        max_price = 0                                                           # Создаем переменную для записи максимального значения
        min_price = 9999                                                        # Создаем переменную для записи минимального значения
        max_date = ''                                                           # Создаем переменную для записи даты максимального значения
        min_date = ''                                                           # Создаем переменную для записи даты минимального значения
        
        for group in gas_list:
            if group[2] == year:                                                # Условие для поиска по году
                price = float(group[3])                                         # Устанавливаем цену переводя в float
                date = '-'.join(group[:3])                                      # Устонавливаем дату переводя из списка в строку для присвоения и вывода строки
                if price > max_price:                                           # Если цена в иттерации больше, то присваиваем макс. дате и числу переменную(они будут обновляться пока ->
                    max_price = price                                           # год не смениться, после смены года будет вывод привязанный к году), тоже самое и с мин. датой и числом
                    max_date = date
                elif price < min_price:
                    min_price = price
                    min_date = date

        print(f'Наибольшая цена в {year} году: {max_price}, {max_date} \n'
              f'Наименьшая цена в {year} году: {min_price}, {min_date}')
        

def generate_max_and_min_sort_file(gas_list):
    price_date_list = []
    price_date_list = [(float(group[3]), '-'.join(group[:3])) for group in gas_list]        # Формируем структуру через list comprehension кортеж, в котором будет первым стоять число
                                                                                            # для дальнейшей сортировки, т.к сортировка идет по первому элементу списка/кортежа
                                                                                            # Обязательно делаем перевод в float и сразу формируем строку под дату
    with open(ASCENDING_FILE, 'w', encoding='utf-8') as file1:
        price_date_list.sort()                                                              # Сортируем от min к max
        for price, date in price_date_list:                                                 # Сразу закрепляем цену и дату за переменными                        
            line = f'{date}:{price}'                                                        # Переменная которая сразу делает готовую для сохранения строку
            file1.write(line + '\n')                                                        # Запись строки в файл
        print('Файл с возрастающим списком сохранен')                                       # Сообщение о завершении

    # Происходит тоже самое что и выше, только сортировка от max к min
    with open(DESCENDING_FILE, 'w', encoding='utf-8') as file2:
        price_date_list.sort(reverse=True)
        for price, date in price_date_list:
            line = f'{date}:{price}'
            file2.write(line + '\n')
        print('Файл с убывающим списком сохранен')
if __name__ == '__main__':
    main()