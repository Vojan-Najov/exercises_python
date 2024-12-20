# А роза упала на лапу Азора 6.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Мы уже писали программы, которые определяли, а палиндром перед нами или нет.
# Давайте теперь найдём все слова-палиндромы среди введённых строк.
# Формат ввода
# Вводятся слова.
# Формат вывода
# Список слов-палиндромов в алфавитном порядке без повторений.
# Примечание
# При проверке слов не обращайте внимание на регистр.
# Пример
# Ввод
# Анна Боря Вова
# Я последняя буква алфавита
# Дед строит шалаш
# Шалаш был хорош
# Дед слышит топот
# Ара залетел в шалаш
# Вывод
# Анна
# Ара
# Дед
# Шалаш
# Я
# в
# топот
# шалаш

from sys import stdin

pollyndroms = set()
for line in stdin:
    for word in line.split():
        if word.lower() == "".join([word[i].lower() for i in range(len(word) - 1, -1, -1)]):
            pollyndroms.add(word)

for p in sorted(pollyndroms):
    print(p)
