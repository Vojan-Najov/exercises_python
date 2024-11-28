# Валидация пароля
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# После того как пользователь ввёл свои данные в требуемом формате, можно
# позаботиться и о пароле.
# Напишите функцию password_validation, которая принимает один позиционный
# параметр — пароль, и следующие именованные параметры:
#     min_length — минимальная длина пароля, по умолчанию 8;
#     possible_chars — строка символов, которые могут быть в пароле, по
#                      умолчанию латинские буквы и цифры;
#     at_least_one — функция возвращающая логическое значение, по умолчанию
#                    str.isdigit.
# Если переданный позиционный параметр не является строкой, вызовите исключение
# TypeError.
# А так же реализуйте собственные исключения:
#     MinLengthError — вызывается, если пароль меньше заданной длины;
#     PossibleCharError — вызывается, если в пароле используется недопустимый
#                         символ;
#     NeedCharError — вызывается, если в пароле не найдено ни одного
#                     обязательного символа.
# Проверка условий должна происходить в порядке указанном в задании.
# Так как, хороший разработчик никогда не хранит пароли в открытом виде,
# функция, в случае успешного завершения, возвращает хеш пароля. Для этого
# воспользуйтесь функцией sha256 из пакета hashlib и верните его
# шестнадцатеричное представление.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# print(password_validation("Hello12345"))
# Вывод
# 67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1
# Пример 2
# Ввод
# print(password_validation(
#     "$uNri$e_777",
#     min_length=6,
#     at_least_one=lambda char: char in "!@#$%^&*()_"
# ))
# Вывод

import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


set_of_chars = {chr(ord('A') + i) for i in range(26)} | \
                {chr(ord('a') + i) for i in range(26)} | \
                {chr(ord('0') + i) for i in range(10)}


def password_validation(password, min_length=8,
                        possible_chars=set_of_chars,
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError('type error')
    if len(password) < min_length:
        raise MinLengthError('min length error')
    if any(smb not in possible_chars for smb in password):
        raise PossibleCharError('possible char error')
    if all(not at_least_one(smb) for smb in password):
        raise NeedCharError('need char error')

    m = hashlib.sha256()
    m.update(bytes(password, encoding='UTF-8'))
    return m.hexdigest()


if __name__ == '__main__':
    try:
        print(password_validation("Hello12345"))
    except Exception as e:
        print(e)

    try:
        print(password_validation(
            "$uNri$e_777",
            min_length=6,
            at_least_one=lambda char: char in "!@#$%^&*()_"
        ))
    except Exception as e:
        print(e)

    try:
        print(password_validation(
            "$uNri$e_777",
            min_length=66,
            at_least_one=lambda char: char in "!@#$%^&*()_"
        ))
    except Exception as e:
        print(e)

    try:
        print(password_validation(
            "uNrieee",
            min_length=6,
        ))
    except Exception as e:
        print(e)







