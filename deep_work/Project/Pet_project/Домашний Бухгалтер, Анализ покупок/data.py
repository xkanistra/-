# Работа с файлами, сохранение и т.п

from config import shoping_tuple
def open_file(): 
    with open(r'Project/Pet_project/Домашний Бухгалтер, Анализ покупок/Список/Список.txt', 'a', encoding='utf-8') as saveList:
        for item in shoping_tuple:
            saveList.write(item + '|')

if __name__ == '__main__':
    open_file()