# Программа расчитывает среднее количество слов в предложении
DATA_FILE = "Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/text.txt"


def main():
    str_file = open_file()
    avg_words = get_words(str_file)


def open_file():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        lines = file.read()
    return lines


def get_words(str_file):
    words = str_file.split()
    total_words = len(words)

    raw_sentences = str_file.split('.')
    sentences = [s.strip() for s in raw_sentences if s.strip()]

    total_sentences = len(sentences)
    avg_words = total_words / total_sentences
    print(f'{total_words} \n {avg_words:.2f}')


if __name__ == "__main__":
    main()
