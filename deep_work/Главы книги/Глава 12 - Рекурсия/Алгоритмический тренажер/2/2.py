def main():
    num = 0
    show_me(num)


def show_me(arg):
    print(arg)
    if arg < 10:
        show_me(arg + 1)


main()
