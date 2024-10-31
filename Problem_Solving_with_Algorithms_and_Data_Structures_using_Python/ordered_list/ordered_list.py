class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = "["
        current = self.head
        while current:
            s += str(current.getData())
            if current.getNext():
                s += ", "
            current = current.getNext()
        s += "]"
        return s

    def isEmpty(self):
        return self.head == None

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False
        while current and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            return
        elif previous == None:
            temp = self.head
            self.head = current.getNext()
            del temp
        else:
            previous.setNext(current.getNext())
            del current

    def index(self, item):
        current = self.head
        index = 0
        found = False
        stop = False
        while current and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                index += 1
                current = current.getNext()

        return index if found else -1


if __name__ == "__main__":

    from random import randrange

    lst = OrderedList()

    print(f"{lst.isEmpty()=}")
    print(f"{lst.size()=}")
    items = []
    for i in range(10):
        item = randrange(100)
        lst.add(item)
        items.append(item)
        print(f"Add {item}:", lst, sep='\n')
    print(f"{lst.isEmpty()=}")
    print(f"{lst.size()=}")
    print()

    print(f"lst.search({items[0]})", "=", lst.search(items[0]))
    print(f"lst.search({items[5]})", "=", lst.search(items[5]))
    print(f"lst.search({items[9]})", "=", lst.search(items[5]))
    print(f"lst.search({items[5] + 1})", "=", lst.search(items[5] + 1))
    print(f"lst.search({items[9] + 1})", "=", lst.search(items[9] + 1))

    lst.remove(items[0])
    lst.remove(items[5])
    lst.remove(items[8])
    lst.remove(items[9])
    print()
    print(lst)


    print(f"lst.index({items[1]})", "=", lst.index(items[1]))
    print(f"lst.index({items[7]})", "=", lst.index(items[7]))
    print(f"lst.index({1000})", "=", lst.index(1000))
