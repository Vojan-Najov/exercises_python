# Рассылка сообщений
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим работу с сервером из прошлой задачи. По пути /users/<id> доступен
# JSON объект пользователя с заданным id.
# Подготовьте текст письма для отправки важной рассылки.
# Если пользователь с заданным идентификатором не найден, выведите сообщение
# «Пользователь не найден».
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке вводится id пользователя, которому требуется отправить письмо.
# В последующих строках записано содержание сообщения с форматированными
# вставками любого из полей объекта.
# Формат вывода
# Выведите подготовленное сообщение.
# Пример 1
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:5000
# 2
# Письмо для: {email}
# Здравствуйте, {last_name} {first_name}
# Мы рады сообщить вам о предстоящей акции!
# Все подробности на нашем сайте
# С уважением, команда тестового сервера!
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
# Письмо для: vas.ivanov@server.none
# Здравствуйте, Иванов Василий
# Мы рады сообщить вам о предстоящей акции!
# Все подробности на нашем сайте
# С уважением, команда тестового сервера!
# Пример 2
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:5000
# 2
# Письмо для: {email}
# Здравствуйте, {last_name} {first_name} ({username})
# Мы рады сообщить вам о предстоящей акции!
# Все подробности на нашем сайте
# С уважением, команда тестового сервера!
# # Данные сервера:
# [
#     {
#         "id": 1,
#         "username": "first",
#         "last_name": "Петрова",
#         "first_name": "Елизавета",
#         "email": "e.petrova@server.none"
#     }
# ]
# Вывод
# Пользователь не найден

from sys import stdin
import requests
import json


url = input()
if not url.startswith('http://'):
    url = 'http://' + url
user_id = int(input())
url += f'/users/{user_id}'
message = stdin.read()

try:
    response = requests.get(url)
    if response.status_code == requests.codes.ALL_OK:
        data = json.loads(response.content)
        message = message.format(**data)
    else:
        message = 'Пользователь не найден\n'
    print(message, end='')

except Exception as e:
    print(e)
