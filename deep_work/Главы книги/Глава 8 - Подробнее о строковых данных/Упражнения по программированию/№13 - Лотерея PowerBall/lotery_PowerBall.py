# Программа выводит числа лотереи по след критериям:
# - 10 наиболее распрастранненых чисел, упорядоченных по частоте
# - 10 наименее распрастранненых чисел, упорядоченных по частоте
# - 10 наиболее "созревших" чисел (чисел, которые не использовались долгое время),
#  упорядоченных от наиболее "созревших" до наименее "созревших"
# - частоту каждого числа от 1 до 69 и частоту каждого PowerBall-числа от 1 до 26


from bisect import bisect_left, bisect_right
from re import split


DATA_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/pbnumbers.txt'
def main():
    pb_file = open_file()
    pb_list = add_list(pb_file)


def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        line = file.readlines()
    return line


def add_list(pb_file):
    pb_list = []
    basic_list = []

    for group in pb_file:
        new_group = group.rstrip()
        split_group = new_group.split(' ')
        pb_list.append(split_group[-1])
        for ch in split_group[:-1]:
            basic_list.append(ch)
    print(pb_list,'\n',basic_list)
    #return pb_list, basic_list


if __name__ == '__main__':
    main()