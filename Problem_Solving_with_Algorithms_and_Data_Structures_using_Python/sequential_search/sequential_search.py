
def sequantial_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        pos += 1

    return found

def ordered_sequantial_search(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        pos += 1

    return found

if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequantial_search(testlist, 3))
    print(sequantial_search(testlist, 13))

    testlist = [i for i in range(0, 100, 2)]
    print(ordered_sequantial_search(testlist, 11))
    print(ordered_sequantial_search(testlist, 20))
