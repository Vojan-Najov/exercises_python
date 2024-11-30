
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def main():
    r = BinaryTree(3)
    print(r)
    insertLeft(r, 4)
    print(r)
    insertLeft(r, 5)
    print(r)
    insertRight(r, 6)
    print(r)
    insertRight(r, 7)
    print(r)
    left = getLeftChild(r)
    print(f'{left=}')

    setRootVal(left, 9)
    print(r)
    insertLeft(left, 11)
    print(r)
    print(getRightChild(getRightChild(r)))

if __name__ == '__main__':
    main()
