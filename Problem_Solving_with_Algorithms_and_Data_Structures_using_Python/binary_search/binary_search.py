
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found

def recursive_binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return recursive_binary_search(alist[:midpoint], item)
        else:
            return recursive_binary_search(alist[midpoint + 1:], item)

if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

    print(f'{binary_search(testlist, 3)=}')
    print(f'{binary_search(testlist, 13)=}')
    print(f'{binary_search(testlist, 0)=}')
    print(f'{binary_search(testlist, -1)=}')
    print(f'{binary_search(testlist, 42)=}')
    print(f'{binary_search(testlist, 45)=}')

    print(f'{recursive_binary_search(testlist, 3)=}')
    print(f'{recursive_binary_search(testlist, 13)=}')
    print(f'{recursive_binary_search(testlist, 0)=}')
    print(f'{recursive_binary_search(testlist, -1)=}')
    print(f'{recursive_binary_search(testlist, 42)=}')
    print(f'{recursive_binary_search(testlist, 45)=}')
