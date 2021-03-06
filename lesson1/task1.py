"""
ЗАДАНИЕ 1

Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек
Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек
"""

print('Привет! Давай посчитаем твое время, которое у тебя есть:)')
seconds = int(input('Просто введи свой интвервал в секундах\n'))
year = seconds // 31536000
month = (seconds // 2592000) % 12
day = (seconds // 86400) % 31
hour = (seconds // 3600) % 24
minute = (seconds // 60) % 60
second = seconds % 60

if seconds < 60:
    print('Итак, у тебя ', second, 'сек')
elif 60 >= seconds < 3600:
    print('Итак, у тебя ', minute, 'мин', second, 'сек')
elif 3600 >= seconds < 86400:
    print('Итак, у тебя ', hour, 'ч', minute, 'мин', second, 'сек')
elif 86400 >= seconds < 2592000:
    print('Итак, у тебя ', day, 'д', hour, 'ч', minute, 'мин', second, 'сек')
elif 2592000 >= seconds < 31536000:
    print('Итак, у тебя ', month, 'мес', day, 'д', hour, 'ч', minute, 'мин', second, 'сек')
elif seconds >= 31536000:
    print('Итак, у тебя ', year, 'г', month, 'мес', day, 'д', hour, 'ч', minute, 'мин', second, 'сек')


"""
Можно ли было просто написать так?
print('Итак, у тебя ', year, 'г', month, 'мес', day, 'д', hour, 'ч', minute, 'м', second, 'с')
"""