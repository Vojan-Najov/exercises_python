# Длины всех слов по чётности
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# В этот раз продумайте функцию length_stats, которая получает текст, а
# возвращает пару объектов Series со словами в качестве индексов и их длинами
# в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от
# знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# odd, even = length_stats('Мама мыла раму')
# print(odd)
# print(even)
# Вывод
# Series([], dtype: int64)
# мама    4
# мыла    4
# раму    4
# dtype: int64
# Пример 2
# Ввод
# odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
# print(odd)
# print(even)
# Вывод
# домик    5
# и        1
# лес      3
# dtype: int64
# зверушка    8
# опушка      6
# странный    8
# dtype: int64

import pandas as pd


def cleaner(word):
    return ''.join(ch.lower() for ch in word if ch.isalpha())


def length_stats(text):
    text = {
        newword: len(newword)
        for newword in sorted(cleaner(word) for word in text.split())
        if newword
    }
    s = pd.Series(text)
    return s[s % 2 == 1], s[s % 2 == 0]
    

def main():
    odd, even = length_stats('Мама мыла раму')
    print(odd)
    print(even)

    odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)



if __name__ == '__main__':
    main()

