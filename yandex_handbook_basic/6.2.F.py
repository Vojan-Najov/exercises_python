# Отчёт успеваемости
# Ограничение времени
# 2 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Во всех без исключения учебных заведениях ведутся журналы успеваемости. Это
# отличный пример данных, подлежащих обработке.
# Рассмотрим журнал летней олимпиадной школы, в которой основными предметами
# выступают математика, физика и информатика. Данные об успеваемости
# представлены DataFrame со столбцами:
#     name — имя;
#     maths — оценка по математике;
#     physics — оценка по физике;
#     computer science — оценка по информатике.
# Напишите функцию best, которая фильтрует всех «ударников» в журнале.
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
# filtered = best(journal)
# print(journal)
# print(filtered)
# Вывод
#        name  maths  physics  computer science
# 0    Иванов      5        4                 5
# 1    Петров      4        4                 2
# 2   Сидоров      5        4                 5
# 3  Васечкин      2        5                 4
# 4  Николаев      4        5                 3
#       name  maths  physics  computer science
# 0   Иванов      5        4                 5
# 2  Сидоров      5        4                 5

import pandas as pd


def best(df):
    return df[df['maths'] > 3][df['physics'] > 3][df['computer science'] > 3]


def main():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)


if __name__ == '__main__':
    main()
