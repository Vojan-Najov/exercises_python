# Регистрация нового пользователя
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим работу с сервером из прошлых задач. При POST запросе по пути
# /users доступна возможность создания новых пользователей. Для этого в данные
# запроса (data) требуется передать JSON объект с информацией о пользователе
# (без указания идентификатора).
# Напишите программу, которая добавляет нового пользователя в систему.
# Формат ввода
# В первой строке вводится адрес сервера.
# В следующих строках вводятся: имя пользователя, фамилия, имя и адрес
# электронной почты.
# Формат вывода
# Ничего выводить не требуется.
# Пример
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:5000
# fourth
# Петров
# Кирилл
# k.petrov@server.none
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
#     },
#     {
#         "username": "fourth",
#         "last_name": "Петров",
#         "first_name": "Кирилл",
#         "email": "k.petrov@server.none",
#         "id": 4
#     }
# ]

import requests
import json


url = input()
if not url.startswith('http://'):
    url = 'http://' + url
url += '/users'

user = {}
user['username'] = input()
user['last_name'] = input()
user['first_name'] = input()
user['email'] = input()

try:
    data = json.dumps(user)
    requests.post(url, data)
except Exception as e:
    print(e)

