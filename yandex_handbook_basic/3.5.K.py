# Файловая статистика 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите программу, которая для заданного файла вычисляет следующие параметры:
#     количество всех чисел;
#     количество положительных чисел;
#     минимальное число;
#     максимальное число;
#     сумма всех чисел;
#     среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# Формат ввода
# Пользователь вводит два имени файла.
# Первый файл содержит произвольное количество чисел, разделённых пробелами и
# символами перевода строки.
# Формат вывода
# Выведите статистику во второй файл в формате JSON.
# Ключи значений задайте соответственно:
#     count — количество всех чисел;
#     positive_count — количество положительных чисел;
#     min — минимальное число;
#     max — максимальное число;
#     sum — сумма всех чисел;
#     average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# Пример
# Ввод
# # Пользовательский ввод:
# numbers.txt
# statistics.json
# # Содержимое файла numbers.txt
# 1 2 3 4 5
# -5 -4 -3 -2 -1
# 10 20
# 20 10
# Вывод
# # Содержимое файла statistics.json
# {
#     "count": 14,
#     "positive_count": 9,
#     "min": -5,
#     "max": 20,
#     "sum": 60,
#     "average": 4.29
# }

import json

statistics = {'count': 0, 'positive_count': 0, 'min': 0,
              'max': 0, 'sum': 0, 'average': 0}

is_first = True
input_filename, output_filename = input(), input()
with open(input_filename, encoding='UTF-8') as input_file:
    for line in input_file:
        for word in line.split():
            num = int(word)
            statistics['count'] += 1
            if num > 0:
                statistics['positive_count'] += 1
            if is_first:
                statistics['min'] = num
                statistics['max'] = num
                is_first = False
            else:
                statistics['min'] = min(statistics['min'], num)
                statistics['max'] = max(statistics['max'], num)
            statistics['sum'] += num
            statistics['average'] = round(statistics['sum'] / statistics['count'], 2)

with open(output_filename, 'w', encoding='UTF-8') as output_file:
    json.dump(statistics, output_file, indent=4)

