# Изменение данных
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим работу с сервером из прошлых задач. При PUT запросе по пути
# /users/<id> доступна возможность изменение информации о пользователе. Для
# этого в данные запроса (data) требуется передать JSON объект с новой
# информацией (без указания идентификатора).
# Напишите программу, которая изменяет информацию о пользователе.
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке записан идентификатор пользователя, информацию о котором
# требуется изменить. В следующих строках вводятся данные для изменения в
# формате: <название поля>=<новое значение>.
# Формат вывода
# Ничего выводить не требуется.
# Пример
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:5000
# 2
# username=ivanov_vasily
# email=ivanov_vasily@server.none
# # Данные сервера:
# [
#     {
#         "id": 1,
#         "username": "first",
#         "last_name": "Петрова",
#         "first_name": "Елизавета",
#         "email": "e.petrova@server.none"
#     },
#     {
#         "id": 2,
#         "username": "second",
#         "last_name": "Иванов",
#         "first_name": "Василий",
#         "email": "vas.ivanov@server.none"
#     },
#     {
#         "id": 3,
#         "username": "third",
#         "last_name": "Иванов",
#         "first_name": "Виктор",
#         "email": "vik.ivanov@server.none"
#     }
# ]
# Вывод
# # Данные сервера:
# [
#     {
#         "id": 1,
#         "username": "first",
#         "last_name": "Петрова",
#         "first_name": "Елизавета",
#         "email": "e.petrova@server.none"
#     },
#     {
#         "id": 2,
#         "username": "ivanov_vasily",
#         "last_name": "Иванов",
#         "first_name": "Василий",
#         "email": "ivanov_vasily@server.none"
#     },
#     {
#         "id": 3,
#         "username": "third",
#         "last_name": "Иванов",
#         "first_name": "Виктор",
#         "email": "vik.ivanov@server.none"
#     }
# ]

from sys import stdin
import requests
import json


url = input()
if not url.startswith('http://'):
    url = 'http://' + url
user_id = input()
url += f'/users/{user_id}'
user_info = {}
while s := stdin.readline():
    key, value = s.strip().split('=')
    user_info[key] = value

try:
    data = json.dumps(user_info)
    requests.put(url, data)
except Exception as e:
    print(e)

