
def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f'Before: {alist}')
    insertion_sort(alist)
    print(f'After : {alist}')
