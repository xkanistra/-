# Программа имитирует викторину для двух игроков


from email.contentmanager import raw_data_manager

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
            split_line = strip_line.split(",")
            question_obj.append(split_line)

    with open(ANSWER_FILE, "r", encoding="utf-8") as load_answer:
        logging.debug("Происходит преображение файла ответов в список...")
        for line in load_answer:
            strip_line = line.rstrip("\n")
            split_line = strip_line.split(",")
            answer_obj.append(split_line)

    logging.info("Функция завершила работу, возврат к выбору действия в меню.\n")
    return question_obj, answer_obj


def set_obj_list(question_obj, answer_obj):
    obj_list = []
    options = []
    question_answer_list = [[q, a] for q, a in zip(question_obj, answer_obj)]

    for item in answer_obj:
        decoy_pool = answer_obj.copy()
        decoy_pool.remove(item)
        sample_pool = random.sample(decoy_pool, 3)
        options = item + sample_pool
        # Продолжи думать как добавить элемент так, чтобы он был либо строкой в списке, либо список в списке
        ## sample_pool.insert(item, 0)

        print(options)


if __name__ == "__main__":
    main()
