# Частотный анализ на минималках
# Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря
# и до шифровальной машины «Энигма». Выполним простой частотный анализ:
# выясним, какой символ встречается в тексте чаще всего.
# Формат ввода
# Вводятся строки, пока не будет введена строка «ФИНИШ».
# Формат вывода
# Выводится один символ в нижнем регистре — наиболее часто встречающийся.
# Примечания
# Пробелы в анализе не участвуют.
# Если в результате анализа получено несколько ответов, следует вывести первый
# по алфавиту.
# Пример 1
# Ввод
# Баобаб
# Белка
# Бобы
# ФИНИШ
# Вывод
# б
# Пример 2
# Ввод
# Финики Фокачча Зайка
# Филин Фосфор Светофор
# Фехтовальщик Форма
# ФИНИШ
# Вывод
# ф
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

tablelen = 26 + 10 + 33
table = [0] * tablelen
while (s := input()) != "ФИНИШ":
    for latter in s:
        latter = latter.lower()
        if latter.isalnum():
            print(latter)
            if ord('a') <= ord(latter) <= ord('z'):
                table[ord(latter) - ord('a')] += 1
            elif ord('0') <= ord(latter) <= ord('9'):
                table[26 + ord(latter) - ord('0')] += 1
            elif ord('а') <= ord(latter) <= ord('я'):
                table[26 + 10 + ord(latter) - ord('а')] += 1

maxcount = table[0]
alpha = 'a'
for i in range(1, tablelen):
    if table[i] > maxcount:
        maxcount = table[i]
        if i < 26:
            alpha = chr(ord('a') + i)
        elif i < 26 + 10:
            alpha = chr(ord('0') + i % 26)
        else:
            alpha = chr(ord('а') + i % (26 + 10))

print(alpha)
