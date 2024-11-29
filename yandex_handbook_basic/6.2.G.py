# Отчёт неуспеваемости
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим обрабатывать DataFrame из прошлой задачи.
# Напишите функцию need_to_work_better, которая выбирает тех, у кого есть хотя
# бы одна двойка.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример
# Ввод
# columns = ['name', 'maths', 'physics', 'computer science']
# data = {
#     'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
#     'maths': [5, 4, 5, 2, 4],
#     'physics': [4, 4, 4, 5, 5],
#     'computer science': [5, 2, 5, 4, 3]
# }
# journal = pd.DataFrame(data, columns=columns)
# filtered = need_to_work_better(journal)
# print(journal)
# print(filtered)
# Вывод
#        name  maths  physics  computer science
# 0    Иванов      5        4                 5
# 1    Петров      4        4                 2
# 2   Сидоров      5        4                 5
# 3  Васечкин      2        5                 4
# 4  Николаев      4        5                 3
#        name  maths  physics  computer science
# 1    Петров      4        4                 2
# 3  Васечкин      2        5                 4

import pandas as pd


def need_to_work_better(df):
    return df[(df['maths'] == 2) | (df['physics'] == 2) | (df['computer science'] == 2)]


def main():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = need_to_work_better(journal)
    print(journal)
    print(filtered)


if __name__ == '__main__':
    main()
