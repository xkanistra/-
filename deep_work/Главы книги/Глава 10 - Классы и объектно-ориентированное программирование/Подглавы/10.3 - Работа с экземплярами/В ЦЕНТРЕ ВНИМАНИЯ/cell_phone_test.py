# Программа тестирует работу класса CellPhone

import cellphone

def main():
    # Получить данные о телефоне
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')   
    retail = float(input('Введите розничную цену: '))

    # Создать экземпляр класса CellPhone
    phone = cellphone.CellPhone(man, mod, retail)

    # Показать введенные данные
    print('Вот введенные Вами данные: ')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')
    
if __name__ == '__main__':
    main()