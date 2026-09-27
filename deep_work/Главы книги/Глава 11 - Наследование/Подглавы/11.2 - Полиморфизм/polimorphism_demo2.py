# Программа демонстрирует полиморфизм

import animals


def main():
    # Создать объект Mammal, Dog
    # и Cat
    mammal = animals.Mammal("это обычное животное")
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном
    print("Вот несколько животных издают и")
    print("звуки, которые они издают.")
    print("--------------------------")
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info("Я - последовательность символов.")


# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы
# show_special и make_sound
def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_special()
        creature.make_sound()
    else:
        print("Это не млекопитающее")


if __name__ == "__main__":
    main()
