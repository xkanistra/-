# Программа получает имя/фамилию/id_номер
# и на их основании создает логин

import login

def main():
    # Получить имя/фамилию/id_номер
    first = input('Введите свое имя: ')
    last = input('Введите свою фамилию: ')
    idnumber = input('Введите свой id_номер: ')

    # Получить логин
    print('Ваше имя для входа в систему: ')
    print(login.get_login_name(first, last, idnumber))

if __name__ == '__main__':
    main()