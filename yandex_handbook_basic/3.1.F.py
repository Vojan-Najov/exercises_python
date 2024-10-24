# Зайка — 6
# Очередное путешествие родителей с детьми, очередная игра с поиском зверушек
# за окном.
# Давайте поиграем и найдём заек.
# Формат ввода
# В первой строке записано натуральное число N — количество выделенных
# придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.
# Формат вывода
# Количество заек.
# Пример 1
# Ввод
# 3
# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка
# Вывод
# 3
# Пример 2
# Ввод
# 4
# зайка березка
# березка зайка
# березка елочка березка
# елочка елочка елочка
# Вывод
# 2
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

n = int(input())
count = 0
for _ in range(n):
    s = input()
    count += s.lower().count("зайка")

print(count)