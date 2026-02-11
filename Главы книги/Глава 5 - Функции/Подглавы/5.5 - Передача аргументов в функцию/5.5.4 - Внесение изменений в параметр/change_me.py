# Программа демонстрирует, что происходит когда
# изменяется значение переменной.

def main():
    value = 99
    print(f'Значение равно {value}')
    change_me(value)
    print(f'После возвращения в функцию main значение равно {value}')

def change_me(arg):
    print('Я изменяю значение.')
    arg = 0
    print(f'Теперь значение равное {arg}.')

main()