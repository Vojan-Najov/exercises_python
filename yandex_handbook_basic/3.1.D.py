# Очистка данных
# Местный провайдер собирает большое количество логов, однако зачастую файлы с
# отчётами приходят в негодность.
# Самые частые проблемы — ошибки вида ## и @@@.
# Напишите программу, которая избавляется от:
#     Двух символов # в начале информационных сообщений;
#     Строк, заканчивающихся тремя символами @.
# Формат ввода
# Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.
# Формат вывода
# Очищенные данные.
# Пример 1
# Ввод
# Hello, world
# Hello, @@@
# ##Goodbye
# Вывод
# Hello, world
# Goodbye
# Пример 2
# Ввод
# First Message
# ##Second Message
# @@@Third Message##
# ##Fourth Message@@@
# Вывод
# First Message
# Second Message
# @@@Third Message##
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

while s := input():
    if s.endswith("@@@"):
        continue
    if s.startswith("##"):
        s = s[2:]
    print(s)
