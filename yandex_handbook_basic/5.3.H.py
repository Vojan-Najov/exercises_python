# Валидация имени пользователя
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим реализацию системы валидации.
# Напишите функцию username_validation, которая принимает один позиционный
# аргумент — имя пользователя:
# Если параметр не является строкой, то вызовите исключение TypeError.
# А также разработайте собственные ошибки:
#     BadCharacterError — вызывается, если значение состоит не только из
#                         латинских букв, цифр и символа нижнего подчёркивания;
#     StartsWithDigitError — вызывается, если значение начинается с цифры.
# Обработка ошибок должна происходить в порядке, указанном в задании.
# В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(username_validation("$user_45$"))
# Вывод
# Вызвано исключение BadCharacterError
# Пример 2
# Ввод
# print(username_validation("45_user"))
# Вывод
# Вызвано исключение StartsWithDigitError

class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError('type error')
    smbs = set('_abcdefghijklmnopqrstuvwxyz0123456789')
    if sum(ord(letter) for letter in username if letter not in smbs):
        raise BadCharacterError('bad character')
    if username[0].isdigit():
        raise StartsWithDigitError('starts with digit')

    return username


if __name__ == '__main__':
    try:
        print(username_validation("$user_45$"))
    except Exception as e:
        print(e)

    try:
        print(username_validation("45_user"))
    except Exception as e:
        print(e)

    try:
        print(username_validation("_user"))
    except Exception as e:
        print(e)

