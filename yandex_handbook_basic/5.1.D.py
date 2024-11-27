# Работа не волк
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Рассмотрим объект «Программист», который задаётся именем, должностью и
# количеством отработанных часов. Каждая должность имеет собственный оклад
# (заработную плату за час работы). В нашей импровизированной компании
# существуют 3 должности:
#     Junior — с окладом 10 тугриков в час;
#     Middle — с окладом 15 тугриков в час;
#     Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое
#              новое повышение.
# Напишите класс Programmer, который инициализируется именем и должностью
# (отработка у нового работника равна нулю). Класс реализует следующие методы:
#     work(time) — отмечает новую отработку в количестве часов time;
#     rise() — повышает программиста;
#     info() — возвращает строку для бухгалтерии в формате:
#            <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример
# Ввод
# programmer = Programmer('Васильев Иван', 'Junior')
# programmer.work(750)
# print(programmer.info())
# programmer.rise()
# programmer.work(500)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# Вывод
# Васильев Иван 750ч. 7500тгр.
# Васильев Иван 1250ч. 15000тгр.
# Васильев Иван 1500ч. 20000тгр.
# Васильев Иван 1750ч. 25250тгр.

class Programmer():
    employee_positions = ['Junior', 'Middle', 'Senior']
    salary_list = [10, 15, 20]

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.salary = \
                Programmer.salary_list[Programmer.employee_positions.index(position)]
        self.savings = 0
        self.time = 0

    def work(self, time):
        self.time += time
        self.savings += self.salary * time

    def rise(self):
        match Programmer.employee_positions.index(self.position):
            case 0:
                self.position = Programmer.employee_positions[1]
                self.salary = Programmer.salary_list[1]
            case 1:
                self.position = Programmer.employee_positions[2]
                self.salary = Programmer.salary_list[2]
            case 2:
                self.salary += 1

    def info(self):
        return F"{self.name} {self.time}ч. {self.savings}тгр."


if __name__ == '__main__':

    programmer = Programmer('Васильев Иван', 'Junior')
    programmer.work(750)
    assert programmer.info() == 'Васильев Иван 750ч. 7500тгр.'

    programmer.rise()
    programmer.work(500)
    assert programmer.info() == 'Васильев Иван 1250ч. 15000тгр.'

    programmer.rise()
    programmer.work(250)
    assert programmer.info() == 'Васильев Иван 1500ч. 20000тгр.'

    programmer.rise()
    programmer.work(250)
    assert programmer.info() == 'Васильев Иван 1750ч. 25250тгр.'
