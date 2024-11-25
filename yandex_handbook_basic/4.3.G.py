# Однотипность не порок
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Во многих задачах требуется контроль входных данных, в частности, несмотря
# на динамическую типизацию, их типов.
# Разработайте декоратор same_type, который производит проверку переменного
# количества позиционных параметров. В случае получения не одинаковых типов
# выводит сообщение "Обнаружены различные типы данных" и прерывает выполнение
# функции.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# @same_type
# def a_plus_b(a, b):
#     return a + b
# print(a_plus_b(3, 5.2) or 'Fail')
# print(a_plus_b(7, '9') or 'Fail')
# print(a_plus_b(-3, 5) or 'Fail')
# Вывод
# Обнаружены различные типы данных
# Fail
# Обнаружены различные типы данных
# Fail
# 2
# Пример 2
# Ввод
# @same_type
# def combine_text(*words):
#     return ' '.join(words)
# print(combine_text('Hello,', 'world!') or 'Fail')
# print(combine_text(2, '+', 2, '=', 4) or 'Fail')
# print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
# Вывод
# Hello, world!
# Обнаружены различные типы данных
# Fail
# Обнаружены различные типы данных
# Fail

def same_type(func):
    def decorated(*args):
        fail = False
        if len(args):
            expected_type = type(args[0])
            for arg in args:
                if not isinstance(arg, expected_type):
                    print('Обнаружены различные типы данных')
                    return

        return func(*args)

    return decorated


if __name__ == '__main__':

    @same_type
    def a_plus_b(a, b):
        return a + b

    print(a_plus_b(3, 5.2) or 'Fail')
    print(a_plus_b(7, '9') or 'Fail')
    print(a_plus_b(-3, 5) or 'Fail')
    # Вывод
    # Обнаружены различные типы данных
    # Fail
    # Обнаружены различные типы данных
    # Fail
    # 2

    print()

    @same_type
    def combine_text(*words):
        return ' '.join(words)

    print(combine_text('Hello,', 'world!') or 'Fail')
    print(combine_text(2, '+', 2, '=', 4) or 'Fail')
    print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
    # Вывод
    # Hello, world!
    # Обнаружены различные типы данных
    # Fail
    # Обнаружены различные типы данных
    # Fail
