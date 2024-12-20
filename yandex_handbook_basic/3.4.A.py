# Автоматизация списка
# Многим весьма часто приходится вести списки продуктов, дел и так далее.
# Напишите программу, которая преобразует введённую строку в нумерованный
# список.
# Формат ввода
# Вводится одна строка.
# Формат вывода
# Требуется вывести нумерованный список, составленный из её слов.
# Пример 1
# Ввод
# картина корзина картонка
# Вывод
# 1. картина
# 2. корзина
# 3. картонка
# Пример 2
# Ввод
# Аня Боря Вова
# Вывод
# 1. Аня
# 2. Боря
# 3. Вова
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

for idx, thing in enumerate(input().split()):
    print(f"{idx + 1}. {thing}")
