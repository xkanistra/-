# Программа переводит дату из формата дд/мм/гг 

def main():
    date_string = get_date()
    date_list = get_list(date_string)
    date_translation = get_translation(date_list)
def get_date():
    date = input('Введите дату в формате дд/мм/гг: ')
    return date

def get_list(date_str):
    date_list = date_str.split('/')
    return date_list

def get_translation(date_list):
    if date_list[1] == '01':
        print(f'{date_list[0]} января {date_list[2]} г.')
    elif date_list[1] == '02':
        print(f'{date_list[0]} февраля {date_list[2]} г.')
    elif date_list[1] == '03':
        print(f'{date_list[0]} марта {date_list[2]} г.')
    elif date_list[1] == '04':
        print(f'{date_list[0]} апреля {date_list[2]} г.')
    elif date_list[1] == '05':
        print(f'{date_list[0]} мая {date_list[2]} г.')
    elif date_list[1] == '06':
        print(f'{date_list[0]} июня {date_list[2]} г.')
    elif date_list[1] == '07':
        print(f'{date_list[0]} июля {date_list[2]} г.')
    elif date_list[1] == '08':
        print(f'{date_list[0]} августа {date_list[2]} г.')
    elif date_list[1] == '09':
        print(f'{date_list[0]} сентября {date_list[2]} г.')
    elif date_list[1] == '10':
        print(f'{date_list[0]} октября {date_list[2]} г.')
    elif date_list[1] == '11':
        print(f'{date_list[0]} ноября {date_list[2]} г.')
    elif date_list[1] == '02':
        print(f'{date_list[0]} декабря {date_list[2]} г.')
        
if __name__ == '__main__':
    main()