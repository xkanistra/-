MIN = 60 
HOUR = 3600 
DAY = 86400 

second = int(input('Введите кол-во секунд '))

if second >= MIN and second < HOUR:
    min = second // MIN
    sec = second % 60
    print(f'{min} минуты, {sec} секунд')

elif second >= 3600 and second < DAY:
    hour = second // HOUR
    min = (second % HOUR) // MIN
    sec = second % 60
    print(f'{hour} часов, {min} минут, {sec} секунд')

elif second >= 86400:
    day = second // DAY
    hour = (second % DAY) // HOUR
    min = (second % HOUR) // MIN
    sec = second % 60
    print(f'{day} день, {hour} часов, {min} минут, {sec} секунд')