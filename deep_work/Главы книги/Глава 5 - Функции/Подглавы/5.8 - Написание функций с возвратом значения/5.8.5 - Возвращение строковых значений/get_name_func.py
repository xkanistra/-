def main():
    name = get_name()
    value = 1520 + 30.6306
    format_value = dollar_format(value)
    print(name, format_value)

def get_name():
    # Получить имя пользователя
    name = input("Введите свое имя: ")
    # Вернуть имя
    return name

def dollar_format(value):
    return f'{value:,.2f}$'

main()
