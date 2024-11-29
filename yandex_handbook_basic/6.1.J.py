# Лесенка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию stairs, принимающую вектор и возвращающую матрицу, в
# которой каждая строка является копией вектора со смещением.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(stairs(np.arange(3)))
# Вывод
# [[0 1 2]
#  [2 0 1]
#  [1 2 0]]
# Пример 2
# Ввод
# print(stairs(np.arange(5)))
# Вывод
# [[0 1 2 3 4]
#  [4 0 1 2 3]
#  [3 4 0 1 2]
#  [2 3 4 0 1]
#  [1 2 3 4 0]]

import numpy as np


def stairs(vec):
    gen = (
        vec[(j - i % len(vec)) % len(vec)]
        for i in range(len(vec))
        for j in range(len(vec))
    )
    return np.array(list(gen)).reshape(len(vec), len(vec))


def main():
    print(stairs(np.arange(3)))
    print(stairs(np.arange(5)))


if __name__ == '__main__':
    main()
