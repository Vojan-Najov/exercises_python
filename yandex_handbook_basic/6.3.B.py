# Суммирование ответов
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите программу, которая суммирует данные, передаваемые с сервера.
# Если сервер передал число 0, значит, данные закончились и он перезапустит
# выдачу ответов.
# Формат ввода
# Вводится адрес сервера.
# Формат вывода
# Одно число — сумма всех данных, полученных с сервера.

import requests


url = input()
if not url.startswith('http://'):
    url = 'http://' + url
try:
    acc = 0
    stop = False
    while not stop:
        response = requests.get(url)
        num = int(response.content.decode(encoding=response.encoding))
        acc += num
        if num == 0:
            stop = True
    print(acc)
except Exception as e:
    print(e)


