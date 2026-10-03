# Программа выводит строку из звездочек от 1 до n звездочек


def main():
    start_len = 1
    end_len = int(input("Введите максимальную длинну строки: "))
    rec_str(start_len, end_len)


def rec_str(start, end):
    if start < end + 1:
        print("*" * start)
        rec_str(start + 1, end)


if __name__ == "__main__":
    main()
