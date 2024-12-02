# run --> PYTHONPATH=$PYTHONPATH:stack:binary_tree python3 ast/ast.py
from stack import Stack
from binary_tree import BinaryTree, preorder, postorder, inorder
import operator


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ('+', '-', '*', '/', ')'):
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ('+', '-', '*', '/'):
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {
        '+': operator.add, 
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


def printexpr(tree):
    sVal = ''
    if tree:
        sVal = '(' + printexpr(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        sVal += printexpr(tree.getRightChild()) + ')'
    return sVal


def main():
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    preorder(pt)
    print()
    postorder(pt)
    print()
    inorder(pt)
    print()
    print(evaluate(pt))
    print()
    print(printexpr(pt))


if __name__ == '__main__':
    main()
