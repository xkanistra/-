import pickle

DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Алгоритмический тренажер/Для решения тренажера/mydata.dat'

def main():
    end_of_file = False
    with open(DATA_FILE, 'rb') as file:
        while not end_of_file:
            try:
                person = pickle.load(file)
                print(person)
            
            except EOFError:
                
                end_of_file = True


if __name__ == '__main__':
    main()