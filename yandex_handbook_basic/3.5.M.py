# Обновление данных
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Часто приходится обновлять данные.
# Создайте программу, которая обновляет JSON файл.
# Формат ввода
# Пользователь вводит имя файла.
# Затем вводятся строки вида ключ == значение.
# Формат вывода
# В заданный пользователем файл следует записать обновленный JSON.
# Пример
# Ввод
# # Пользовательский ввод:
# data.json
# one == один
# two == два
# three == три
# # Содержимое файла data.json
# {
#     "one": 1,
#     "three": 2
# }
# Вывод
# # Содержимое файла data.json
# {
#     "one": "один",
#     "three": "три",
#     "two": "два"
# }

import json
from sys import stdin

filename = input()
with open(filename, 'r', encoding='UTF-8') as input_file:
    global record
    record = json.load(input_file)

for line in stdin:
    key, value = line.strip().split(" == ")
    record[key] = value

with open(filename, "w", encoding='UTF-8') as output_file:
    json.dump(record, output_file, ensure_ascii=False, indent=4)

