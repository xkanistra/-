# Программа считывает и выводит данные о населении США
DATA_FILE = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/USPopulation.txt'
START_YEAR = 1950
def main():
    population_list = []
    population_list = add_list()
    population = calculate(population_list)

def add_list():
    index = 0
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        population = file.readlines()

    while index < len(population):
        population[index] = int(population[index])
        index += 1
    return population

def calculate(population_list):
    total_calculate = 0
    total = 0

    for item in population_list:
        total_calculate += item
        total += 1
    average = total_calculate / total
    min_Population_yaer = min(population_list)
    max_Population_yaer = max(population_list)
    min_idex = population_list.index(min_Population_yaer)
    max_index = population_list.index(max_Population_yaer)
    print(f'Среднегодовое увеличение: {average}\n'
          f'Год с минимальным увеличением: {START_YEAR + min_idex} год\n'
          f'Год с максимальным увеличение: {START_YEAR + max_index} год')
    
if __name__ == '__main__':
    main()