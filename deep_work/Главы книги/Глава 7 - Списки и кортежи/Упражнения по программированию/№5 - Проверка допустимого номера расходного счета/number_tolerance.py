# Программа ищет необходимый счет среди списка
DATA_FILE = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/charge_accounts.txt'
def main():
    accounts_list = add_list()
    print(accounts_list)
    search(accounts_list)

def add_list():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        accounts = file.readlines()

    index = 0
    while index < len(accounts):
        accounts[index] = int(accounts[index])
        index += 1
    return accounts

def search(accounts_list):
    again = 'д'
    while again == 'д' or again == 'Д':

        search = int(input('Введите номер счета: '))
        if search in accounts_list:
            print(f'Номер {search} допустим')
            again = input('Желаете продолжить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break

        else:
            print(f'Номер {search} недопустим')
            again = input('Желаете повторить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break

if __name__ == '__main__':
    main()