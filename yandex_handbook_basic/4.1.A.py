# Функциональное приветствие
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Большинство задач этой главы ориентировано на отработку навыков по разработке
# функций.
# Ваше решение будет использоваться как библиотека.
# Напишите функцию print_hello, которая принимает имя пользователя и выводит
# приветствие в стандартный поток вывода.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# name = "world"
# print_hello(name)
# Вывод
# Hello, world!
# Пример 2
# Ввод
# string = "Yandex"
# print_hello(string)
# Вывод
# Hello, Yandex!

from sys import stdin

def print_hello(string):
    print(f'Hello, {string}!')

prog = stdin.read()
exec(prog)
