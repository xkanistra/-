def main():
    num = int(input("Введите число"))
    traffic_sign(num)


def traffic_sign(n):
    if n > 0:
        print("Не парковаться")
        traffic_sign(n - 1)


main()
