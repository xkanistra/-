# Имитация предсказывания случайных ответов / Не доделал
import random
DATA_FILE = "Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/8_ball_responses_ru.txt"

def main():
    response_list = []
    response_list = add_list()
    choice = get_choice(response_list)
    print
def add_list():
    with open(DATA_FILE, "r") as file:
        response = file.readlines()

    index = 0
    while index < len(response):
        response[index] = response[index].rstrip("\n")
        index += 1
    return response

def get_choice(response_list):
    again = 'д'
    while again == 'д' == 'Д':
        index = random.randint(11)
        response = response_list[index]
        choice = input('Задайте вопрос: ')
        again = input('Введите Д/д для следующего вопроса:')
    return response
if __name__ == "__main__":
    main()
