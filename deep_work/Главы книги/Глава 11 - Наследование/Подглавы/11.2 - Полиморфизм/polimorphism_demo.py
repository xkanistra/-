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

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы
# show_special и make_sound
def show_mammal_info(creature):
    creature.show_special()
    creature.make_sound()


if __name__ == '__main__':
    main()