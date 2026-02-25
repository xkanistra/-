# Игра камень/ножницы/бумага
import random

def main():
    move = random.randint(1, 3)
    computer = computer_move(move)
    user = user_move()
    print(f'Компьютер: {computer}')
    print(f'Вы: {user}')
    if computer == 'Камень' and user == 'Камень' or computer == 'Ножницы' and user == 'Ножницы' or computer == 'Бумага' and user == 'Бумага':
        print('Ничья: сыграйте еще раунд.')
    elif computer == 'Камень' and user == 'Ножницы':
        print('Вы проиграли.')
    elif computer == 'Камень' and user == 'Бумага':
        print('Вы победили.')
    elif computer == 'Ножницы' and user == 'Бумага':
        print('Вы проиграли.')
    elif computer == 'Бумага' and user == 'Ножницы':
        print('Вы победили.')
        
def computer_move(move):
    if move == 1:
        status = 'Камень'
        return status
    elif move == 2:
        status = 'Ножницы'
        return status
    elif move == 3:
        status = 'Бумага'
        return status
        
def user_move():
    menu()
    move = int(input('Выберите действие:'))
    if move == 1:
        status = 'Камень'
        return status
    elif move == 2:
        status = 'Ножницы'
        return status
    elif move == 3:
        status = 'Бумага'
        return status
        
def menu():
    print('1. Камень')
    print('2. Ножницы')
    print('3. Бумага')

main()