# Программа корректирует текст делая буквы верхним регистром где это необходимо
import re

DATA_FILE = "Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/text.txt"


def main():
    user_text = input_text()
    corrector = corrector_str(user_text)


def input_text():
    text = input("Введите ваше сообщение: ")
    return text


def corrector_str(usr_text):
    corrector = []
    raw_text = re.split(r"[.!?]", usr_text)
    text = [s.strip() for s in raw_text if s.strip()]



if __name__ == "__main__":
    main()
