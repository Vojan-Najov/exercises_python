# Валидация пользователя
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Используйте две предыдущих функции валидации и напишите функцию
# user_validation, которая принимает именованныеаргументы:
#     last_name — фамилия;
#     first_name — имя;
#     username — имя пользователя.
# Если функции был передан неизвестный параметр или не передан один из
# обязательных, то вызовите исключение KeyError.
# Если один из параметров не является строкой, то вызовите исключение TypeError.
# Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.
# Если поле заполнено верно, функция возвращает словарь с данными пользователя.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
# Вывод
# {'last_name': 'Иванов', 'first_name': 'Иван', 'username': 'ivanych45'}
# Пример 2
# Ввод
# print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
# Вывод
# Вызвано исключение KeyError

class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def user_validation_check_kwarg(**kwargs):
    set_of_args = {'last_name', 'first_name', 'username'}
    for key in kwargs:
        if key not in set_of_args:
            return False
        set_of_args.remove(key)

    if len(set_of_args):
        return False
    return True


def name_validation(name):
    first = True
    for letter in name:
        if letter.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщыъьэюя':
            raise CyrillicError('cyrillic error')
        if first and letter.islower() or not first and letter.isupper():
            raise CapitalError('capital error')
        first = False

    return name


def username_validation(username):
    smbs = set('_abcdefghijklmnopqrstuvwxyz0123456789')
    if sum(ord(letter) for letter in username if letter.lower() not in smbs):
        raise BadCharacterError('bad character')
    if username[0].isdigit():
        raise StartsWithDigitError('starts with digit')

    return username


def user_validation(**kwargs):
    if not user_validation_check_kwarg(**kwargs):
        raise KeyError('key error')

    if any(not isinstance(value, str) for value in kwargs.values()):
        raise TypeError('type error')

    name_validation(kwargs['last_name'])  
    name_validation(kwargs['first_name'])  
    username_validation(kwargs['username'])

    return kwargs


if __name__ == '__main__':
    try:
        user_validation(tmp=1)
    except Exception as e:
        print(e)

    try:
        user_validation(last_name="Иванов", first_name="Иван",
                        username="ivanych45", tmp=1)
    except Exception as e:
        print(e)

    try:
        user_validation(last_name="Иванов", first_name="Иван")
    except Exception as e:
        print(e)

    try:
        user_validation(last_name="Иванов", first_name="Иван",
                        username=11)
    except Exception as e:
        print(e)

    try:
        print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
    except Exception as e:
        print(e)
        
    try:
        print(user_validation(last_name="Иванов", first_name="Иван",
                              username="ivanych45", password="123456"))
    except Exception as e:
        print(e)

