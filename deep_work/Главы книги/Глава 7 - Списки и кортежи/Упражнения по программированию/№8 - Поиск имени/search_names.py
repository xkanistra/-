# Программа ищет имя среди двух списков
DATA_BOYS = "Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/BoyNames.txt"
DATA_GIRLS = "Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/GirlNames.txt"


def main():
    boys_list = []
    girls_list = []
    boys_list, girls_list = add_list()
    search = search_list(boys_list, girls_list)

def add_list():
    index = 0
    with open(DATA_BOYS, "r", encoding="utf-8") as boysFile:
        boys = boysFile.readlines()
    with open(DATA_GIRLS, "r", encoding="utf-8") as girlsFile:
        girls = girlsFile.readlines()

    while index < len(boys) and index < len(girls):
        boys[index] = boys[index].rstrip('\n')
        girls[index] = girls[index].rstrip('\n')
        index += 1

    return boys, girls

def search_list(boys_list, girls_list):
    again = 'д'
    while again == 'Д' or again == 'д':
        search_boy = input('Введите имя мальчка(Enter если пропустить): ')
        search_girl = input('Введите имя девочки(Enter если пропустить): ')
        if search_boy in boys_list or search_girl in girls_list:
            print('Введенные имена есть в списке популярных имен')
            print()
            again = input('Желаете продолжить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break
        else:
            print('Введенных имен нет в списке популярных имен')
            print()
            again = input('Желаете повторить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break


if __name__ == "__main__":
    main()


