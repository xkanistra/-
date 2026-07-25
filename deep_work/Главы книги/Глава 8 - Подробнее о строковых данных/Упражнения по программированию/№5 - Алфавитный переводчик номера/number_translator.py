# Программа переводит номер из формата XXX-XXX-XXXX
# в числовой
NUM_TUPLE = (
    ("2", "A", "B", "C"),
    ("3", "D", "E", "F"), 
    ("4", "G", "H", "I"),
    ("5", "J", "K", "L"), 
    ("6", "M", "N", "O"),
    ("7", "P", "Q", "R", "S"),
    ("8", "T", "U", "V"),
    ("9", "W", "X", "Y", "Z")
)


def main():
    number = input_number()
    translate_number(number)


def input_number():
    number = input("Введите номер в формате XXX-XXX-XXXX: ")
    return number


def translate_number(number):
    result = []
    for item in number:
        ch = item.upper()
        if item == '-':
            result.append(item)
        else:
            for group in NUM_TUPLE:
                if ch in group:
                    result.append(group[0])
                    break

    print(''.join(result))


if __name__ == "__main__":
    main()
