# Модернизация системы вывода
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Разработайте функцию modern_print, которая принимает строку и выводит её,
# если она не была выведена ранее.
# Примечание
# В решении не должно быть вызовов требуемых функций.
# Пример 1
# Ввод
# modern_print("Hello!")
# modern_print("Hello!")
# modern_print("How do you do?")
# modern_print("Hello!")
# Вывод
# Hello!
# How do you do?
# Пример 2
# Ввод
# modern_print("Ало!")
# modern_print("Ало!")
# modern_print("Я тебя не слышу")
# modern_print("Ало!")
# modern_print("Ало!")
# modern_print("Позвони когда сможешь")
# modern_print("Позвони когда сможешь")
# modern_print("Я тебя не слышу")
# Вывод
# Ало!
# Я тебя не слышу
# Позвони когда сможешь

phrases = set()

def modern_print(string):
    global phrases
    if string not in phrases:
        print(string)
    phrases.add(string)

if __name__ == '__main__':
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Я тебя не слышу")
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Позвони когда сможешь")
    modern_print("Позвони когда сможешь")
    modern_print("Я тебя не слышу")

