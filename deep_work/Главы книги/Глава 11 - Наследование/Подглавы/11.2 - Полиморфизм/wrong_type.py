def main():
    # Передать символьные значения в функцию show_mammal_info
    show_mammal_info("Я - последовательность символов.")


# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы
# show_special и make_sound
def show_mammal_info(creature):
    creature.show_special()
    creature.make_sound()


if __name__ == "__main__":
    main()
