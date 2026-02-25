# Игра угадай число
import random

def main():
    main_menu()
    number = random.randint(1, 100)
  
    total = 0
    while True:
        input_number = int(input('Введите число: '))
        if input_number > number:
            print(get_more())
            total += 1
        elif input_number < number:
            print(get_less())
            total +=1
        else: 
            print(get_equally())
            print(f'Всего попыток: {total}')
            break
            
def main_menu():
    print('Игра угадай число')
    print('Загадано число от 1 - 100')
   
def get_more():
    return 'Слишком много, попробуйте еще раз'
    
def get_less():
    return 'Слишком мало, попробуйте еще раз'
    
def get_equally():
    return 'Поздравляем, вы верно угадали число!'
    
main()