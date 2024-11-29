# Числовая змейка 3.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её
# на основе массивов.
# Напишите функцию snake, которая принимает ширину (M) и высоту (N) змейки, а
# также именованный параметр direction.
# Параметр direction могут принимать значения:
#     H — горизонтальная змейка, используется по умолчанию;
#     V — вертикальная змейка.
# Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(snake(5, 3))
# Вывод
# [[ 1  2  3  4  5]
#  [10  9  8  7  6]
#  [11 12 13 14 15]]
# Пример 2
# Ввод
# print(snake(5, 3, direction='V'))
# Вывод
# [[ 1  6  7 12 13]
#  [ 2  5  8 11 14]
#  [ 3  4  9 10 15]]

import numpy as np


def snake(m, n, direction='H'):
    gen = (for i in range(n) for range(1, m + 1))

    return np.array(list(gen), dtype='int16').reshape(n, m)


def main()
    print(snake(5, 3))


if __name__ == '__main__':
    main()
