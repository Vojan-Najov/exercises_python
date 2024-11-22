# Имя of the month
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Разработайте функцию month, которая принимает номер месяца и обозначение
# языка ("ru", "en") и возвращает название заданного месяца в заданном языке с
# заглавной буквы.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# result = month(1, "en")
# Вывод
# result = 'January'
# Пример 2
# Ввод
# result = month(7, "ru")
# Вывод
# result = 'Июль'

def month(number, lang):
    dictionary = {
            'ru': ['Январь', 'Февраль', 'Март', 'Апрель',
                   'Май', 'Июнь', 'Июль', 'Август',
                   'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
            'en': ['January', 'February', 'March', 'April',
                   'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December'],
            }

    return dictionary[lang][number - 1]

if __name__ == '__main__':
    assert month(1, 'en') == 'January'
    assert month(7, 'ru') == 'Июль'
