# Программа считает сколько лет была победителем выбранная команда
DATA_FILE = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/WorldSeriesWinners.txt'

def main():
    winner_list = []
    winner_list = add_list()
    search, total_year = search_winners(winner_list)
    if total_year < 4:
        print(f'Команда {search} побеждала {total_year} года')
    else:
        print(f'Команда {search} побеждала {total_year} лет')

def search_winners(winners):
    total_year = 0
    search = input(f'Впишите название команды: ')
    for item in winners:
        if search == item:
            total_year += 1
    return search, total_year
def add_list():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        winners = file.readlines()

    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip('\n')
        index += 1

    return winners

if __name__ == '__main__':
    main()