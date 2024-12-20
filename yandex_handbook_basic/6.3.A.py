# Проверка системы
# Ограничение времени
# 5 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# В локальной сети тестирующей системы работает сервер 127.0.0.1.
# Он слушает порт 5000 и иногда отвечает на него.
# Обратитесь к серверу и выведите сообщение, полученное от него.
# Примечания
#     Во всех задачах данной главы используется протокол http
#     Не забудьте, что ответ сервера является бинарным объектом и его следует
#     декодировать.
# Пример 1
# Ввод
# # Пользовательский ввод:
# # Данные сервера:
# Привет!
# Вывод
# Привет!
# Пример 2
# Ввод
# # Пользовательский ввод:
# # Данные сервера:
# Сервер работает в штатном режиме
# Вывод
# Сервер работает в штатном режиме

import requests

try:
    response = requests.get('http://127.0.0.1:5000')
    print(response.content.decode(encoding=response.encoding))
except Exception as e:
    print(e)

