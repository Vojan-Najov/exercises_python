# Суммирование ответов 3
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Сервер отвечает на несколько путей, каждый из которых возвращает свой JSON
# список. Напишите программу, которая произведёт сбор и суммирование всех
# данных по заданным путям.
# Формат ввода
# Вводится адрес сервера и список анализируемых путей.
# Формат вывода
# Одно число — сумма всех чисел из полученных списков.
# Пример 1
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:5000
# /first
# /third
# # Данные сервера:
# /first -> [1, 2, 3]
# /second -> [2, 4, 6]
# /third -> [3, 6, 9]
# Вывод
# 24
# Пример 2
# Ввод
# # Пользовательский ввод:
# 127.0.0.1:8080
# /second
# # Данные сервера:
# /first -> [1, 2, 3]
# /second -> [2, 4, 6]
# /third -> [3, 6, 9]
# Вывод
# 12

from sys import stdin
import requests
import json


url = input()
if not url.startswith('http://'):
    url = 'http://' + url
paths = []
while s := stdin.readline():
    s = s.strip()
    if s:
        paths.append(s)

print(url, paths)

acc = 0
try:
    for path in paths:
        response = requests.get(url + path)
        data = json.loads(response.content)
        acc += sum(data)
    print(acc)
except Exception as e:
    print(e)
