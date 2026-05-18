# Программа получает пароль и проверяет его

from login2 import valid_password

def main():
    # Получить пароль
    password = input('Введите свой пароль: ')

    # Проверить допустимость пароля
    while not valid_password(password):
        print('Этот пароль недопустим')
        password = input('Введите свой пароль: ')
    
    print('Это допустимый пароль')

if __name__ == '__main__':
    main()