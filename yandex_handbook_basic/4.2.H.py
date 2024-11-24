# Длинная сортировка
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Напишите lambda выражение для сортировки списка слов сначала по длине, а
# затем по алфавиту без учёта регистра.
# Примечание
# В решении не должно быть ничего, кроме выражения.
# Пример 1
# Ввод
# string = 'мама мыла раму'
# print(sorted(string.split(), key=<ваше выражение>))
# Вывод
# ['мама', 'мыла', 'раму']
# Пример 2
# Ввод
# string = 'Яндекс использует Python во многих проектах'
# print(sorted(string.split(), key=<ваше выражение>))
# Вывод
# ['во', 'Python', 'многих', 'Яндекс', 'проектах', 'использует']

mykey = lambda line: (len(line), line.lower())

string = 'мама мыла раму'
print(sorted(string.split(), key=mykey))

string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=mykey))
