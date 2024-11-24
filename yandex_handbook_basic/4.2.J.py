# Ключевой секрет
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Вася любит секреты и шифрование. Он часто пользуется шифром на основе замен и
# просит разработать вас функцию, которая позволит ему быстро шифровать сообщения.
# Напишите функцию secret_replace(text, **replaces), которая принимает:
#     текст требующий шифрования;
#     именованные аргументы — правила замен, представляющие собой кортежи из
#                             одного или нескольких значений.
# Функция должна вернуть зашифрованный текст.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Обратите внимание, что позиционный аргумент требуемой функции не должен иметь
# однобуквенного имени. Для понимания ошибки исследуйте следующих код:
# def func(a, **b):
#     ...
# func(1, **{'a': 2})
# Пример 1
# Ввод
# result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
# Вывод
# result = 'Hehiy123, wzrhid!'
# Пример 2
# Ввод
# result = secret_replace(
#     "ABRA-KADABRA",
#     A=("Z", "1", "!"),
#     B=("3",),
#     R=("X", "7"),
#     K=("G", "H"),
#     D=("0", "2"),
# )
# Вывод
# result = 'Z3X1-G!0Z371'

def secret_replace(string, **kwargs):
    d = {}
    secret_string = ""
    for letter in string:
        if letter in kwargs:
            idx = d.get(letter, 0)
            repls = kwargs[letter]
            repl = repls[idx]
            d[letter] = (idx + 1) % (len(repls))
            secret_string += repl
        else:
            secret_string += letter

    return secret_string

if __name__ == '__main__':
    result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
    assert result == 'Hehiy123, wzrhid!'

    result = secret_replace(
        "ABRA-KADABRA",
        A=("Z", "1", "!"),
        B=("3",),
        R=("X", "7"),
        K=("G", "H"),
        D=("0", "2"),
    )
    assert result == 'Z3X1-G!0Z371'
