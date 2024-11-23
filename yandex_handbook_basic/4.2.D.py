# Имя of the month 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Разработайте функцию month, которая возвращает название заданного месяца с
# заглавной буквы. Функция должна принимать номер месяца и дополнительно
# обозначение языка (по умолчанию "ru").
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
# result = month(7)
# Вывод
# result = 'Июль'

def month(number, lang='ru'):
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
    assert month(7) == 'Июль'