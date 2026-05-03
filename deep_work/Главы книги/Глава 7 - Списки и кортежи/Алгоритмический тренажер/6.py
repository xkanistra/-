def main():
    names = ["Кирилл", "Руби", "Вова", "Сергей", "Влад"]
    print(names)
    print()

    search = input("Введите имя которое хотите найти в списке: ")

    if search in names:
        print(f"Привет, {search}")
    else:
        print(f"{search} отсутствует")


if __name__ == "__main__":
    main()
