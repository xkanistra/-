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


logging.debug("Это отладочное сообщение")
logging.info("Информационное сообщение")
logging.warning("Предупреждение")
logging.error("Ошибка")
logging.critical("Критическая ошибка\n")


# Главная функция
def main():
    logging.info("Программа запущенна.\n")
    logging.info("Вызов функции load_item().")
    question_obj, answer_obj = load_item()
    logging.info("Вызов функции set_obj_list().")
    obj_list = set_obj_list(question_obj, answer_obj)
    logging.info("Вызов функции play_quiz().")
    play_quiz(obj_list)
    logging.info('Программа завершена.')

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


# Функция set_obj_list() парсит файлы и создает список объектов Question
def set_obj_list(question_obj, answer_obj):
    logging.info("Функция set_obj_list() запущена.")
    logging.debug("Создан пустой список для объектов.")
    obj_list = []

    # Использую метод zip и list compression для простого заполнения
    # списка [[Вопрос, ответ]].
    logging.debug("Создание вложенного списка [[Вопрос, ответ]].")
    question_answer_list = [[q, a] for q, a in zip(question_obj, answer_obj)]

    # Циклом проходим по вложенному списку, благодаря тому,
    # что пары вопрос/ответ являются одними объектами списка
    # отсутствует необходимость в введение пременной для подсчета индекса
    logging.info("Запуск парсера...")
    for qst, answ in question_answer_list:
        # Копия необходима для удаления из пула ответов
        # повторов правильных вариантов через remove
        decoy_pool = answer_obj.copy()
        decoy_pool.remove(answ)
        logging.debug(f"Создана копия списка ответов без повторов\n{decoy_pool}")

        # Использую sample для перемешивания нужного кол-ва элементов списка
        # без изменения основного списка, в отличии от shuffle.
        # Затем использую insert т.к хочу добавить на нужный индекс верный ответ
        sample_pool = random.sample(decoy_pool, 3)
        sample_pool.insert(0, answ)

        # sample снова перемешиваю
        random_pool = random.sample(sample_pool, 4)

        position_index = random_pool.index(answ)
        true_num = position_index + 1
        logging.debug(f"Ответы перемешенны:{random_pool}\nВерный №{true_num}")

        # Создаю объект класса Question в сразу добавляя его в список
        # удаляю не нужный в дальнейшем код
        obj_list.append(
            question.Question(
                qst,
                random_pool[0],
                random_pool[1],
                random_pool[2],
                random_pool[3],
                true_num,
            )
        )

    logging.info(f"Парсер завершен. Объектов создано: {len(obj_list)}\n")
    return obj_list


# Функция play_quiz() нужна для работы самой игры и её логики
def play_quiz(obj_list):
    logging.info("Функция play_quiz() запущена.")
    # Создаю список для учета очков двух игроков
    logging.debug("Создан список учета очков.")
    scores = [0, 0]

    # Использую метод enumerate для удобного отслеживания
    # номера итерации цикла в index, quiz использую для
    # отслеживания объектов
    logging.info("Запущен цикл виктрины.")
    for index, quiz in enumerate(obj_list):
        # Использую деление с остатком для удобного отслеживания номера игрока
        # это избавляет от кучи if-elif-else
        player = index % 2
        print(f"Вопрос №{index + 1}")

        if player == 0:
            logging.info(f"Отвечает игрок 1")
            print(f"Вопрос игроку {player + 1}:\n{quiz.get_question()}")
            print()
            print(f"Варианты ответа:")
            # Циклом вывожу варианты ответов вместо 4 print'ов\
            # указываю в start с какого числа начинать отсчет итераций,
            # избавляет от написания переменной счетчика
            logging.info("Показаны варианты ответов игрока 1.")
            for num, answer in enumerate(quiz.get_answer_list(), start=1):
                print(f"{num}. {answer}")

            # Использую try/except для защиты от ввода неверного формата в переменную
            try:
                logging.info("Игрок 1 дает свой ответ.")
                choice = int(input(f"Ответ игрока {player + 1}: "))
                # Циклом while валидирую ввод данных в нужном диапазоне
                while choice < 1 or choice > 4:
                    choice = int(
                        input(
                            f"Игрок {player + 1}, введите представленные номера ответов 1 - 4: "
                        )
                    )
                if choice == quiz.get_num_true_answer():
                    quiz.show_true_anser(quiz.get_answer_list()[choice - 1])
                    scores[player] += 1
                    logging.info(f"Игрок 1 ответил верно, счет : {scores}\n")
                else:
                    print("Ответ не верный\n")
                    logging.info(f"Игрок 1 ответил не верно, счет : {scores}\n")
            except ValueError:
                logging.error(f"Игрок 1 ввел неверный тип данный: {choice}\n")
                print(
                    f"Введите допустимый вариант ввода: 1 - 4\n"
                    f"Вы пропускаете вопрос.\n"
                )

        else:
            logging.info(f"Отвечает игрок 2")
            print(f"Вопрос игроку {player + 1}:\n{quiz.get_question()}")
            print()
            print(f"Варианты ответа:\n")
            # Циклом вывожу варианты ответов вместо 4 print'ов\
            # указываю в start с какого числа начинать отсчет итераций,
            # избавляет от написания переменной счетчика
            logging.info("Показаны варианты ответов игрока 2.")
            for num, answer in enumerate(quiz.get_answer_list(), start=1):
                print(f"{num}. {answer}")

            # Использую try/except для защиты от ввода неверного формата в переменную
            try:
                logging.info("Игрок 2 дает свой ответ.")
                choice = int(input(f"Ответ игрока {player + 1}: "))
                # Циклом while валидирую ввод данных в нужном диапазоне
                while choice < 1 or choice > 4:
                    choice = int(
                        input(
                            f"Игрок {player + 1}, введите представленные номера ответов 1 - 4: "
                        )
                    )
                if choice == quiz.get_num_true_answer():
                    quiz.show_true_anser(quiz.get_answer_list()[choice - 1])
                    scores[player] += 1
                    logging.info(f'Игрок 2 ответил верно, счет : {scores}\n')
                else:
                    print("Ответ не верный\n")
                    logging.info(f"Игрок 2 ответил не верно, счет : {scores}\n")
            except ValueError:
                logging.error(f"Игрок 2 ввел неверный тип данный: {choice}\n")
                print(
                    f"Введите допустимый вариант ввода: 1 - 4\n"
                    f"Вы пропускаете вопрос.\n"
                )

    logging.info('Вопросы закончились\nПодсчет итогов.')

    # Использования созданного списка позволяет легко по индексу 
    # сравнивать итоги, без вввода дополнительных переменных
    print("Игрок 1\t: Игрок 2")
    print(f"{scores[0]}\t: {scores[1]}")
    if scores[0] > scores[1]:
        logging.info(f'Победа игрока 1: {scores}')
        print("Победил игрок 1")
    elif scores[0] == scores[1]:
        logging.info(f'Ничья: {scores}')
        print("Ничья!")
    else:
        logging.info(f'Победа игрока 2: {scores}')
        print("Победил игрок 2")

    logging.info('Функция завершена.\n')


if __name__ == "__main__":
    main()
