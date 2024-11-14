# Сборы на прогулку
# Воспитатель в детском саду устал тратить время, чтобы построить детей по
# парам.
# Он договорился с детьми, чтобы те делились на две, по возможности равные,
# группы.
# Напишите программу, которая по списку двух шеренг составляет пары детей.
# Формат ввода
# Вводится две строки с именами детей, записанными через запятую и пробел.
# Формат вывода
# Требуется вывести список пар, которые можно составить, если последовательно
# брать из каждой шеренги по одному ребёнку.
# Имена в парах выводить через дефис окружённый пробелами.
# Примечание
# В одной из групп может быть на одного ребенка больше, чем в другой.
# Этот ребёнок при формировании пар не учитывается и идёт в паре с воспитателем.
# Пример
# Ввод
# Аня, Вова
# Боря, Дима, Гена
# Вывод
# Аня - Боря
# Вова - Дима
# Ограничение памяти
# 64.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

for p1, p2 in zip(input().split(", "), input().split(", ")):
    print(f"{p1} - {p2}")
