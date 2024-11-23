
def selection_sort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        position_of_max = 0

        for location in range(1, fillslot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        alist[fillslot], alist[position_of_max] = alist[position_of_max], alist[fillslot]

def selection_sort_with_min(alist):
    for i in range(len(alist) - 1):
        index_of_min = i
        
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[index_of_min]:
                index_of_min = j

        if index_of_min != i:
            alist[i], alist[index_of_min] = alist[index_of_min], alist[i]
    

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f'Before: {alist}')
    selection_sort(alist)
    print(f'After : {alist}')

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f'Before: {alist}')
    selection_sort_with_min(alist)
    print(f'After : {alist}')
