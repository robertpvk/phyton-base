"""
Задание 2

Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
дополнить числа до двух разрядов нулём!

"""

# Так можно было?)
# list_one = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# list_one[1] = '"05"'
# list_one[3] = '"17"'
# list_one[8]= '"+05"'
# print(' '.join(list_one))

list_one = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

digits = []

for symbol in list_one:
    if symbol.isdigit():
        digits.extend(['""' + f'{int(symbol):02}' + '""'])
    elif symbol[0] == '+' or symbol[0] == '-':
        s = symbol[0]
        digits.extend(['""' + s + f'{int(symbol[1:]):02}' + '""'])
    else:
        digits.append(symbol)

end = ' '.join(digits)
print(end)
