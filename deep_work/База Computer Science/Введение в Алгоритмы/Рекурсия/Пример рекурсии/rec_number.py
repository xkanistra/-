# Вывод чисел от 1 до 10 рекурсивно
MAX_NUM = 10
MIN_NUM = 1


def main():
    not_recursion()
    print()
    recursion(MIN_NUM)


def not_recursion():
    for i in range(1, MAX_NUM + 1):
        print(i, end=" ")
    

def recursion(num):
    if num == MAX_NUM + 1:
        return 1
    print(num, end=" ")
    return recursion(num + 1)


if __name__ == "__main__":
    main()
