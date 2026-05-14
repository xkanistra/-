# Имитация предсказывания случайных ответов 
import random
DATA_FILE = "Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/8_ball_responses_ru.txt"

def main():
    again = 'Д'
    response_list = []
    response_list = add_list()
    while again == 'Д' or again == 'д':
        choice = get_choice(response_list)
        print(choice)
        again = input('Введите Д/д для следующего вопроса:') 
        if again == 'Д' or again == 'д':
            again = 'д'
        else:
            print('Приходите еще!')
            break

def add_list():
    with open(DATA_FILE, "r") as file:
        response = file.readlines()

    index = 0
    while index < len(response):
        response[index] = response[index].rstrip("\n")
        index += 1
    return response

def get_choice(response_list):
    choice = input('Задайте вопрос: ')
    index = random.randint(0, 11)
    response = response_list[index] 
    return response
             
if __name__ == "__main__":
    main()
