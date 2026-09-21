# Программа имитирует викторину для двух игроков


import question
import logging
import random

# Глобальная константа имени файла
LOGGER_FILE = "Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№9 - Викторина/app.log"
QUESTION_FILE = "Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№9 - Викторина/question.txt"
ANSWER_FILE = "Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№9 - Викторина/answer.txt"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -> %(message)s",
    filename=LOGGER_FILE,
    filemode="a",
)


def main():
    question_obj, answer_obj = load_item()
    obj_list = set_obj_list(question_obj, answer_obj)
    play_quiz(obj_list)


# Функция load_item() загружает информацию из файла
# и передает её в качестве списка объектов
def load_item():
    logging.info("Функция load_item() начинает считывание файлов...")
    logging.debug("Созданы пустые списоки для объектов .")
    question_obj = []
    answer_obj = []

    with open(QUESTION_FILE, "r", encoding="utf-8") as load_question:
        logging.debug("Происходит преображение файла вопросов в список...")
        for line in load_question:
            strip_line = line.rstrip("\n")
            question_obj.append(strip_line)

    with open(ANSWER_FILE, "r", encoding="utf-8") as load_answer:
        logging.debug("Происходит преображение файла ответов в список...")
        for line in load_answer:
            strip_line = line.rstrip("\n")
            answer_obj.append(strip_line)

    logging.info("Функция завершила работу, возврат к выбору действия в меню.\n")
    return question_obj, answer_obj


def set_obj_list(question_obj, answer_obj):
    obj_list = []
    question_answer_list = [[q, a] for q, a in zip(question_obj, answer_obj)]

    for qst, answ in question_answer_list:
        decoy_pool = answer_obj.copy()
        decoy_pool.remove(answ)

        sample_pool = random.sample(decoy_pool, 3)
        sample_pool.insert(0, answ)

        random_pool = random.sample(sample_pool, 4)

        position_index = random_pool.index(answ)
        true_num = position_index + 1

        quiz_obj = question.Question(
            qst,
            random_pool[0],
            random_pool[1],
            random_pool[2],
            random_pool[3],
            true_num,
        )
        obj_list.append(quiz_obj)

        return obj_list


def play_quiz(obj_list):
    scores = [0, 0]
    # Тут подумай почему не повторяется цикл а прерывается
    for index, quiz in enumerate(obj_list, 1):
        player = index % 2
        if player == 0:
            print(f"Вопрос игроку {player}:\n{quiz.get_question()}")
            print()
            print(f"Варианты ответа:")
            for num, answer in enumerate(quiz.get_answer_list(), start=1):
                print(f"{num}. {answer}")
            # Добавть try/except + валидацию ввода
            choice = int(input(f"Ответ игрока {player}: "))
            if choice == quiz.get_num_true_answer():
                quiz.show_true_anser(quiz.get_answer_list()[choice - 1])
                scores[player] += 1
        else:
            print(f"Вопрос игроку {player}:\n{quiz.get_question()}")
            print()
            print(f"Варианты ответа:")
            for num, answer in enumerate(quiz.get_answer_list(), start=1):
                print(f"{num}. {answer}")
            # Добавть try/except + валидацию ввода
            choice = int(input(f"Ответ игрока {player}: "))
            if choice == quiz.get_num_true_answer():
                quiz.show_true_anser(quiz.get_answer_list()[choice - 1])
                scores[player] += 1

    # Тут подумай как вывести победителя
    #for player_1, player_2 in scores:
        #print(f'{player_1} : {player_2}')
        #if player_1 > player_2:
            #print('Победил игрок 1') 


if __name__ == "__main__":
    main()
