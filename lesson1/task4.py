"""
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""
print('1 процент', '2 процента', '3 процента', '4 процента', sep='\n')
for i in range(5, 101):
    print(str(i) + ' процентов', sep='\n')