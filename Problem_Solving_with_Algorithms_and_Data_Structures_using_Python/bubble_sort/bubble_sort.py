
def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f'Before: {alist}')
    bubble_sort(alist)
    print(f' After: {alist}')

    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    print(f'Before: {alist}')
    short_bubble_sort(alist)
    print(f' After: {alist}')
