# Длинные слова
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Фильтрация данных — одна из первостепенных задач их анализа.
# Напишите функцию get_long, принимающую серию формата первой задачи и
# фильтрующую её по именованному параметру min_length (по умолчанию 5).
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
# filtered = get_long(data)
# print(data)
# print(filtered)
# Вывод
# мир       3
# питон     5
# привет    6
# яндекс    6
# dtype: int64
# питон     5
# привет    6
# яндекс    6
# dtype: int64
# Пример 2
# Ввод
# data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
# filtered = get_long(data, min_length=6)
# print(data)
# print(filtered)
# Вывод
# мир       3
# питон     5
# привет    6
# яндекс    6
# dtype: int64
# привет    6
# яндекс    6
# dtype: int64

import pandas as pd


def get_long(words_seria, min_length=5):
    return words_seria[words_seria >= min_length]


def main():
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data)
    print(data)
    print(filtered)

    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data, min_length=6)
    print(data)
    print(filtered)

if __name__ == '__main__':
    main()
