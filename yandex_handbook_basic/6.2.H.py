# Обновление журнала
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим обрабатывать DataFrame из прошлых задач.
# Напишите функцию update, которая добавляет к данным столбец average,
# содержащий среднюю оценку ученика, а также сортирует данные по убыванию
# этого столбца, а при равенстве средних — по имени лексикографически.
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
# filtered = update(journal)
# print(journal)
# print(filtered)
# Вывод
#        name  maths  physics  computer science
# 0    Иванов      5        4                 5
# 1    Петров      4        4                 2
# 2   Сидоров      5        4                 5
# 3  Васечкин      2        5                 4
# 4  Николаев      4        5                 3
#        name  maths  physics  computer science   average
# 0    Иванов      5        4                 5  4.666667
# 2   Сидоров      5        4                 5  4.666667
# 4  Николаев      4        5                 3  4.000000
# 3  Васечкин      2        5                 4  3.666667
# 1    Петров      4        4                 2  3.333333

import pandas as pd


def update(df):
    return df.assign(
        average=lambda x: (x['maths'] + x['physics'] + x['computer science']) / 3
    ).sort_values(
        ['average', 'name'],
        ascending=[False, True]
    )


def main():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаед', 'Николаев'],
        'maths': [5, 4, 5, 2, 4, 4],
        'physics': [4, 4, 4, 5, 5, 5],
        'computer science': [5, 2, 5, 4, 3, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)


if __name__ == '__main__':
    main()
