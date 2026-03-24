# Программа записывает мои имя фамилия в файл и сохр его

def main():
    try:
        name_file = open('my_name.txt', 'w')

        first_name = input('Введите ваше имя:')
        last_name = input('Введите вашу фамилию:')

        name_file.write(f'{first_name}\n')
        name_file.write(f'{last_name}\n')

        name_file.close
    
    except:
        print('Произошла ошибка')
    else:
        print('Данные сохранены в файл')

if __name__ == '__main__':
    main()

