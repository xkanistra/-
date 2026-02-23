# Программа дает пользователю ввести ответ на математический тест
import random

def main():
    main_menu()
    random_num1 = get_random_num1()
    random_num2 = get_random_num2()
    result = random_num1 + random_num2
    total = int(input('Введите ответ: '))
    if total != result:
        print(f'Ответ неверный.')
        print(f'Правильный ответ: {result}') 
    else:
            print(f'Поздравляем, вы ответили верно!')
            print(f'{result}')
    
def main_menu():
    print('-' * 8, 'Тест', '-' * 8)
    print('Решите приведенный ниже пример')

def get_random_num1():
    result = random.randint(100, 300)
    print(result)
    return result
    
def get_random_num2():
    result = random.randint(100, 300)
    print('+',result)
    return result
    
main()