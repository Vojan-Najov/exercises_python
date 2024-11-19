# Слияние данных
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Одна местная компания производит обновление данных о пользователях и заодно
# решили реорганизовать систему хранения.
# Напишите программу, которая обновляет данные о пользователях, записанных в
# JSON файле.
# Формат ввода
# Пользователь вводит два имени файла.
# В первом хранится JSON массив пользователей.
# Во втором — массив новых данных.
# Информация о каждом пользователе представляется JSON объектом, в котором
# обязательно присутствует поле name, описывающее имя пользователя. Остальные
# поля являются дополнительными.
# Формат вывода
# В первый файл запишите информацию о пользователях в виде JSON объекта,
# ключами которого выступают имена пользователей, а значениями — объекты с
# информацией о них.
# Если какая-либо дополнительная информация о пользователе изменяется, то
# требуется сохранить лексикографически большее значение.
# Пример
# Ввод
# # Пользовательский ввод:
# users.json
# updates.json
# # Содержимое файла users.json
# [
#     {
#         "name": "Ann",
#         "address": "Flower st."
#     },
#     {
#         "name": "Bob",
#         "address": "Summer st.",
#         "phone": "+7 (123) 456-78-90"
#     }
# ]
# # Содержимое файла updates.json
# [
#     {
#         "name": "Ann",
#         "address": "Awesome st.",
#         "phone": "+7 (098) 765-43-21"
#     },
#     {
#         "name": "Bob",
#         "address": "Winter st."
#     }
# ]
# Вывод
# # Содержимое файла users.json
# {
#     "Ann": {
#         "address": "Flower st.",
#         "phone": "+7 (098) 765-43-21"
#     },
#     "Bob": {
#         "address": "Winter st.",
#         "phone": "+7 (123) 456-78-90"
#     }
# }

import json

users_filename = input()
updates_filename = input()

with open(users_filename, 'r', encoding='UTF-8') as users_file:
    global users
    records = json.load(users_file)

with open(updates_filename, 'r', encoding='UTF-8') as updates_file:
    global updates
    updates = json.load(updates_file)

users = {}
for record in records:
    name = record['name']
    del record['name']
    users[name] = {**record}

for update in updates:
    name = update['name']
    del update['name']
    for k, v in update.items():
        if k not in users[name] or users[name][k] < v:
            users[name][k] = v

with open(users_filename, 'w', encoding='UTF-8') as users_file:
    json.dump(users, users_file, ensure_ascii=False, indent=4)

