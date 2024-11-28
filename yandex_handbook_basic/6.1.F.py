# Не решена
# Матрица умножения
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию multiplication_matrix, которая принимает размер матрицы (N)
# и возвращает массив описывающий таблицу умножения N на N.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(multiplication_matrix(3))
# Вывод
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]
# Пример 2
# Ввод
# print(multiplication_matrix(5))
# Вывод
# [[ 1  2  3  4  5]
#  [ 2  4  6  8 10]
#  [ 3  6  9 12 15]
#  [ 4  8 12 16 20]
#  [ 5 10 15 20 25]]

import numpy as np


def multiplication_matrix(n):
    return np.array([i * j for i in range(1, n + 1) for j in range(1, n + 1)]).reshape(n, n)


def main():
    print(multiplication_matrix(3))
    print(multiplication_matrix(5))


if __name__ == '__main__':
    main()
