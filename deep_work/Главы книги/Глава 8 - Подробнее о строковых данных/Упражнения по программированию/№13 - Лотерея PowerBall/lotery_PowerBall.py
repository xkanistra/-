# Программа выводит числа лотереи по след критериям:
# - 10 наиболее распрастранненых чисел, упорядоченных по частоте
# - 10 наименее распрастранненых чисел, упорядоченных по частоте
# - 10 наиболее "созревших" чисел (чисел, которые не использовались долгое время),
#  упорядоченных от наиболее "созревших" до наименее "созревших"
# - частоту каждого числа от 1 до 69 и частоту каждого PowerBall-числа от 1 до 26


DATA_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/pbnumbers.txt'

def main():
    pb_file = open_file()
    pb_list, basic_list, num_list = add_list(pb_file)
    pb_sort_list, basic_sort_list = add_count_number(pb_list, basic_list)
    pb_mature, basic_mature = find_mature_numbers(num_list)
    get_ansewr(pb_sort_list, basic_sort_list, pb_mature, basic_mature)

def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        line = file.readlines()

    return line


def add_list(pb_file):
    pb_list = []
    basic_list = []
    num_list = []
    for group in pb_file:
        new_group = group.rstrip()
        split_group = new_group.split(' ')
        num_list.append(split_group)
        pb_list.append(split_group[-1])
        for ch in split_group[:-1]:
            basic_list.append(ch)

    return pb_list, basic_list, num_list


def find_mature_numbers(num_list):
    pb_last_seen = [0] * 26
    basic_last_seen = [0] * 69
    TOTAL_DRAWS = len(num_list) 

    # Алгоритм присвоения похож на алгоритм из add_count_number
    for draw_number, draw_numbers in enumerate(num_list, 1):
        pb_num = int(draw_numbers[-1])
        pb_last_seen[pb_num - 1] = draw_number

        for num_str in draw_numbers[:-1]:
            basic_num = int(num_str)
            basic_last_seen[basic_num - 1] = draw_number
    
    pb_mature = [(TOTAL_DRAWS - last_seen, index + 1) for index, last_seen in enumerate(pb_last_seen)]
    basic_mature = [(TOTAL_DRAWS - last_seen, index + 1) for index, last_seen in enumerate(basic_last_seen)]
    pb_mature.sort(reverse=True)
    basic_mature.sort(reverse=True)
    
    return pb_mature, basic_mature


def add_count_number(pb_list, basic_list):
    pb_count = [0] * 26
    basic_count = [0] * 69

    for i in pb_list:
        num = int(i)
        pb_count[num - 1] += 1
        
    for i in basic_list:
        num = int(i)
        basic_count[num - 1] += 1

    pb_sort_list = [(counter, index + 1) for index, counter in enumerate(pb_count)]
    basic_sort_list = [(counter, index + 1) for index, counter in enumerate(basic_count)]
    pb_sort_list.sort()
    basic_sort_list.sort()
    return pb_sort_list, basic_sort_list


def get_ansewr(pb_sort_list, basic_sort_list, pb_mature, basic_mature):
    pb_reverse  = pb_sort_list[::-1]
    basic_reverse = basic_sort_list[::-1]
    print('=' * 5, 'Топ 10 самых частых номеров PowerBall', '=' * 5)
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