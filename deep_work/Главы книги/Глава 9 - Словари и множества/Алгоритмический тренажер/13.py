import pickle

DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Алгоритмический тренажер/Для решения тренажера/mydata.dat'

def main():
    dct = {'Глеб':15, 'Кирилл':21, 'Лиза':20, 'Денис':41}
    with open(DATA_FILE, 'wb') as file:
            pickle.dump(dct, file)
        

if __name__ == '__main__':
    main()