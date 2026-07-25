# Программа выводит числа лотереи по след критериям:
# - 10 наиболее распрастранненых чисел, упорядоченных по частоте
# - 10 наименее распрастранненых чисел, упорядоченных по частоте
# - 10 наиболее "созревших" чисел (чисел, которые не использовались долгое время),
#  упорядоченных от наиболее "созревших" до наименее "созревших"
# - частоту каждого числа от 1 до 69 и частоту каждого PowerBall-числа от 1 до 26

# Константа для удобства доступа к файлу для его открытия
DATA_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/pbnumbers.txt'

def main():
    pb_file = open_file()
    pb_list, basic_list, num_list = add_list(pb_file)
    pb_sort_list, basic_sort_list = add_count_number(pb_list, basic_list)
    pb_mature, basic_mature = find_mature_numbers(num_list)
    get_ansewr(pb_sort_list, basic_sort_list, pb_mature, basic_mature)

def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:                        # Открываем файл через with чтобы вручную его не закрывать, кодировка UTF-8
        line = file.readlines()                                                 # Читаем весь файл через readlines, чтобы каждая строка стала списком внутри списка (не удаляет \n)

    return line                                                                 # Возвращаем список


def add_list(pb_file):
    pb_list = []
    basic_list = []
    num_list = []
    for group in pb_file:                                                       # Читаем список в цикле передавая каждый вложенный список в group при иттерации -> становится строкой
        new_group = group.rstrip()                                              # rstrip удаляет \n из строки
        split_group = new_group.split(' ')                                      # Разделяем каждую строку через пробел чтобы разделить значения строке 1 2 3 -> [1], [2], [3] 
        num_list.append(split_group)                                            # Добавляем каждое значение в список 
        pb_list.append(split_group[-1])                                         # Добавляем только последнее/PowerBall значение 
        for ch in split_group[:-1]:                                             # Читаем срез без последнего значения, чтобы добавить все значения кроме PowerBall
            basic_list.append(ch)

    return pb_list, basic_list, num_list                                        # Возвращаем списоки


def find_mature_numbers(num_list):
    pb_last_seen = [0] * 26                                                     # Дублируем через * чтобы вручную не писать 26 [0]
    basic_last_seen = [0] * 69                                                  # Дублируем через * чтобы вручную не писать 69 [0]
    TOTAL_DRAWS = len(num_list)                                                 # Константа для показывающая кол-во розыгрышей

    # Алгоритм присвоения похож на алгоритм из add_count_number
    for draw_number, draw_numbers in enumerate(num_list, 1):                    # Две переменных для enumerate, draw_number - Номер розыгрыша, draw_numbers - список чисел в розыгрыше,  
                                                                                # num_list - список номеров в каждом розыгрыше, 1 - номер с котого начинается счет(если не указывать будет 0) 
        pb_num = int(draw_numbers[-1])                                          # Переводим из строки в число для получения числа PowerBall
        pb_last_seen[pb_num - 1] = draw_number                                  # Присваиваем в списке(номер розыгрыша, номер) позиции "номер розыгрыша" значение

        for num_str in draw_numbers[:-1]:                                       # Тоже самое для полного списка
            basic_num = int(num_str)
            basic_last_seen[basic_num - 1] = draw_number
    
    # Формируем структуру через list comprehension чтобы не писать большие циклы for создаем списки упорядоченных по частоте появления значений (когда последний раз был розыгрыш, номер)
    # index, last_seen - переменные для enumerate, pb_last_seen - список из которого мы берем значения для index, last_seen
    # index - является номером, last_seen = draw_number
    pb_mature = [(TOTAL_DRAWS - last_seen, index + 1) for index, last_seen in enumerate(pb_last_seen)]
    basic_mature = [(TOTAL_DRAWS - last_seen, index + 1) for index, last_seen in enumerate(basic_last_seen)]
    pb_mature.sort(reverse=True)                                                # Реверсивно сортируем(чтобы не использовать отдельно sort и потом reverse)
    basic_mature.sort(reverse=True)
    
    return pb_mature, basic_mature


def add_count_number(pb_list, basic_list):
    # Тут такая же логика для создания вложенного списка (кол-во повторений, номер)
    pb_count = [0] * 26
    basic_count = [0] * 69

    for i in pb_list:
        num = int(i)
        # += вместо =, чтобы увеличивать счетчик для отслеживания кол-ва повторений номера
        pb_count[num - 1] += 1
        
    for i in basic_list:
        num = int(i)
        basic_count[num - 1] += 1

    # Такая же логика что и выше для формирования структуру списка
    pb_sort_list = [(counter, index + 1) for index, counter in enumerate(pb_count)]
    basic_sort_list = [(counter, index + 1) for index, counter in enumerate(basic_count)]
    pb_sort_list.sort()
    basic_sort_list.sort()
    return pb_sort_list, basic_sort_list


def get_ansewr(pb_sort_list, basic_sort_list, pb_mature, basic_mature):
    # Создание копий списка только реверсивного для самых частых элементов, т.к списки выше отсортированны по возрастанию от min к max
    pb_reverse  = pb_sort_list[::-1]                                            
    basic_reverse = basic_sort_list[::-1]                                       
    print('=' * 5, 'Топ 10 самых частых номеров PowerBall', '=' * 5)
    # В цикле выводим через enumerate, где 
    # top_pb - номер в выводе (вместо top_pb =  0 и top_pb += 1)
    # counter, number срез из кортежа, который взяли в pb_reverse, в кортеже идет (количество повторений, номер) ->
    # counter - количество повторений, number - номер, далее меняется лишь список из которого берем значения и размер среза(при необходимости)
    for top_pb, (counter, number) in enumerate(pb_reverse[:10], 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ 10 самых редких номеров PowerBall', '=' * 5)
    for top_pb, (counter, number) in enumerate(pb_sort_list[:10], 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ 10 самых частых номеров', '=' * 5)
    for top_pb, (counter, number) in enumerate(basic_reverse[:10], 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ 10 самых редких номеров', '=' * 5)
    for top_pb, (counter, number) in enumerate(basic_sort_list[:10], 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ номеров PowerBall', '=' * 5)
    for top_pb, (counter, number) in enumerate(pb_sort_list, 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ всех номеров', '=' * 5)
    for top_pb, (counter, number) in enumerate(basic_sort_list, 1):
        print(f'{top_pb}. № {number} - {counter} раз')

    print()

    print('=' * 5, 'Топ 10 наиболее созревших номеров PowerBall', '=' * 5)
    for top_pb, (counter, number) in enumerate(pb_mature[:10], 1):
        print(f'{top_pb}. № {number} - {counter} игр назад')

    print()

    print('=' * 5, 'Топ 10 наиболее созревших номеров', '=' * 5)
    for top_pb, (counter, number) in enumerate(basic_mature[:10], 1):
        print(f'{top_pb}. № {number} - {counter} игр назад')

if __name__ == '__main__':
    main()