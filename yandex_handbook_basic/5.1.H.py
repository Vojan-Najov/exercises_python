# Шашки
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Шашки очень занимательная игра, которую достаточно легко моделировать.
# Правила подразумевают наличие двух классов: игральная доска и шашка. Однако
# мы немного упростим себе задачу и вместо шашки будем манипулировать клетками,
# которые могут находиться в трех состояниях: пустая, белая шашка и чёрная шашка.
# Разработайте два класса: Checkers и Cell.
# Объекты класса Checkers при инициализации строят игральную доску со
# стандартным распределением клеток и должны обладать методами:
#     move(f, t) — перемещает шашку из позиции f в позицию t;
#     get_cell(p) — возвращает объект «клетка» в позиции p.
# Объекты класса Cell при инициализации принимают одно из трех состояний:
#   W — белая шашка, B — чёрная шашка, X — пустая клетка,
# а также обладают методом status() возвращающим заложенное в ней состояние.
# Координаты клеток описываются строками вида PQ, где:
#     P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
#     Q — строка игральной доски, одна из цифр: 12345678.
# Будем считать, что пользователь всегда ходит правильно и контролировать
# возможность хода не требуется.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# checkers = Checkers()
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()
# Вывод
# XBXBXBXB
# BXBXBXBX
# XBXBXBXB
# XXXXXXXX
# XXXXXXXX
# WXWXWXWX
# XWXWXWXW
# WXWXWXWX
# Пример 2
# Ввод
# checkers = Checkers()
# checkers.move('C3', 'D4')
# checkers.move('H6', 'G5')
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()
# Вывод
# XBXBXBXB
# BXBXBXBX
# XBXBXBXX
# XXXXXXBX
# XXXWXXXX
# WXXXWXWX
# XWXWXWXW
# WXWXWXWX

class Cell():
    
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers():
    start_state = [
        'XBXBXBXB',
        'BXBXBXBX',
        'XBXBXBXB',
        'XXXXXXXX',
        'XXXXXXXX',
        'WXWXWXWX',
        'XWXWXWXW',
        'WXWXWXWX'
    ]

    def __init__(self):
        self.state = [[Cell(state) for state in row] for row in reversed(Checkers.start_state)]

    def get_cell(self, p):
        col = ord(p[0]) - ord('A')
        row = ord(p[1]) - ord('1')
        return self.state[row][col]

    def move(self, f, t):
        from_col, from_row = ord(f[0]) - ord('A'), ord(f[1]) - ord('1')
        to_col, to_row = ord(t[0]) - ord('A'), ord(t[1]) - ord('1')
        self.state[to_row][to_col] = self.state[from_row][from_col]
        self.state[from_row][from_col] = Cell('X')
        

if __name__ == '__main__':
    checkers = Checkers()
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()

    print()

    checkers = Checkers()
    checkers.move('C3', 'D4')
    checkers.move('H6', 'G5')
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()

