# Валидация имени
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# При регистрации в различных сервисах пользователи вводят большое количество
# информации. Правильное заполнение полей — важная часть работы программы,
# поэтому формы снабжают системами валидации данных.
# Напишите функцию name_validation, которая принимает один позиционный аргумент
# — фамилию или имя.
# Если параметр не является строкой, то вызовите исключение TypeError.
# А также разработайте собственные ошибки:
#     CyrillicError — вызывается, если значение не состоит только из
#                     кириллических букв;
#     CapitalError — вызывается, если значение не начинается с заглавной буквы
#                    или найдена заглавная буква не в начале значения.
# Обработка ошибок должна происходить в порядке, указанном в задании.
# В случае успешного выполнения, функция должна вернуть переданный параметр
# без изменений.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(name_validation("user"))
# Вывод
# Вызвано исключение CyrillicError
# Пример 2
# Ввод
# print(name_validation("иванов"))
# Вывод
# Вызвано исключение CapitalError

class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    first = True
    for letter in name:
        if letter.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщыъьэюя':
            raise CyrillicError('cyrillic error')
        if first and letter.islower() or not first and letter.isupper():
            raise CapitalError('capital error')
        first = False

    return name


if __name__ == '__main__':
    try:
        print(name_validation("user"))
    except Exception as e:
        print(e)

    try:
        print(name_validation("иванов"))
    except Exception as e:
        print(e)


