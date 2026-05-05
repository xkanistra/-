# Генерирование лотерейных билетов
import random
NUMBERS = 7
MIN_NUM = 0
MAX_NUM = 9
DATA_LIST = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Решение для задач/Лотерейные билеты.txt' 

def main():
    random_list = []
    for num in range(0, NUMBERS + 1):
        number = random.randint(MIN_NUM, MAX_NUM + 1)
        random_list.append(number)
    
    for item in random_list:
        print(item, end='')

    save_file(random_list)

def save_file(list):
    with open(DATA_LIST, 'a', encoding='utf-8') as file:
        for item in list:
            file.write(str(item))
        file.write('\n')
if __name__ == '__main__':
    main()