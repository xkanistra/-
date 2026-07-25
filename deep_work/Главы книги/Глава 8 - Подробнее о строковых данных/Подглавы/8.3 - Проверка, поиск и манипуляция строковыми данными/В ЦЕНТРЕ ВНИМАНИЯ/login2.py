# Функция get_login_name принимает имя, фамилию
# и инд.номер в качестве аргументов
# Возвращает имя для входа в систему

def get_login_name(first, last, idnumber):
    # Получить первые 3 буквы имени
    # если длинна меньше 3 то вернуть имя
    set1 = first[0 : 3]

    # Получить первые 3 буквы фамилии
    # если длинна меньше 3 то вернуть всю фамилию
    set2 = last[0 : 3]

    # Получить первые 3 цифры инд номера
    # если длинна меньше 3 то вернуть весь номер
    set3 = idnumber[-3 : ]

    # Собрать логин
    login_name = set1 + set2 + set3

    return login_name

# Функция valid_password принимает пароль
# в качестве аргумента и возвращает True/False
# сообщая о допустимости пароля
# Он допустим если 
# - Содержать минимум 7 символ
# - Содержать минимум одну буквы в верхнем регистре
# - Содержать минимум одну буквы в нижнем регистре
# - Содержать минимум одну цифру

def valid_password(password):
    # Назначить булевым переменным значение False
    correct_lenght = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Приступить к валидации
    # Проверка длинны
    if len(password) >= 7:
        correct_lenght = True
        # Анализ каждого символа и установка флага
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

        # Определить удовлетворены ли все требования
        # Если да то is_valid = True
        # Иначе is_valid = False
        if correct_lenght and has_uppercase and has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        return is_valid