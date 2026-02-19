# Написать функцию get_first_name которая просит ввести свео имя и возвращает его

def main():
    name = get_first_name()
    print(name)
def get_first_name():
    first = input('Введите свое имя: ')
    return first

main()