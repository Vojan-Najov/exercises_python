# Вращение
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите функцию rotate, принимающую двумерную матрицу и один из углов
# поворота: 90°, 180°, 270° и 360°.
# Функция должна вернуть новую матрицу соответствующую заданному повороту по
# часовой стрелке.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(rotate(np.arange(12).reshape(3, 4), 90))
# Вывод
# [[ 8  4  0]
#  [ 9  5  1]
#  [10  6  2]
#  [11  7  3]]
# Пример 2
# Ввод
# print(rotate(np.arange(12).reshape(3, 4), 270))
# Вывод
# [[ 3  7 11]
#  [ 2  6 10]
#  [ 1  5  9]
#  [ 0  4  8]]

import numpy as np


def rotate(matrix, angle):
    if angle <= 180:
        while angle > 0:
            matrix = np.rot90(matrix, -1)
            angle -= 90
    else:
        angle -= 360
        while angle < 0:
            matrix = np.rot90(matrix)
            angle += 90
    return matrix



def main():
    print(rotate(np.arange(12).reshape(3, 4), 90))
    print(rotate(np.arange(12).reshape(3, 4), 270))


if __name__ == '__main__':
    main()
