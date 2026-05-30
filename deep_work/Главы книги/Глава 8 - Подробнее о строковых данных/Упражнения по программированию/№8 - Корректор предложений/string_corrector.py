# Программа корректирует текст делая буквы верхним регистром где это необходимо
import re


def main():
    user_text = input_text()
    result = corrector_str(user_text)
    print(result)

def input_text():
    text = input("Введите ваше сообщение: ")
    return text


def corrector_str(usr_text):
    corrector = []
    finaly = []
    raw_text = re.split(r"[.!?]", usr_text)
    text = [s.strip() for s in raw_text if s.strip()]
    for group in text:
        corrector.append(group.upper()[:1] + group[1:] + '.')
    return ' '.join(corrector)


if __name__ == "__main__":
    main()
