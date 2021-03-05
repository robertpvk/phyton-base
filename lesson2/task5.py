"""
Задание 5
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
Например:
57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...

Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).

Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).

Создать новый список, содержащий те же цены, но отсортированные по убыванию.

Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""


goods = [57.8, 46.51, 97, 10.2, 7.7, 23.5, 55, 21.22, 39.3, 22.2]
print(id(goods))
goods.sort()
print(id(goods))

print()


for good in goods:
    rubles = int(good)
    pennys = int(good * 100) % 100
    print(f'{rubles} руб {pennys:02} коп')


print()


goods_second = [57.8, 46.51, 97, 10.2, 7.7, 23.5, 55, 21.22, 39.3, 22.2]
goods_second.sort(reverse=True)
for good_second in goods_second:
    rubles = int(good_second)
    pennys = int(good_second * 100) % 100
    print(f'{rubles} руб {pennys:02} коп')


print()


for good in goods[-5:]:
    rubles = int(good)
    pennys = int(good * 100) % 100
    print(f'{rubles} руб {pennys:02} коп')
