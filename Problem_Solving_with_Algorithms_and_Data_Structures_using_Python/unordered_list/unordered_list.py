
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


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        s = "["
        cur = self.head
        while cur:
            s += str(cur.getData())
            cur = cur.getNext()
            s += ", " if cur else ""
        s += "]"
        return s


    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.getNext()
        return count

    def search(self, item):
        cur = self.head
        found = False
        while cur and not found:
            found = cur.getData() == item
            cur = cur.getNext()
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while cur and not found:
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()

        if not found:
            return
        elif prev == None:
            temp = self.head
            self.head = cur.getNext()
            del temp
        else:
            prev.setNext(cur.getNext())
            del cur

    def append(self, item):
        temp = Node(item)
        cur = self.head

        if not self.head:
            self.head = temp
        else:
            while cur.getNext():
                cur = cur.getNext()
            cur.setNext(temp)

    def index(self, item):
        cur = self.head
        index = 0
        found = False
        while cur and not found:
            if cur.getData() == item:
                found = True
            else:
                index += 1
                cur = cur.getNext()
        return index if found else -1

    def insert(self, pos, item):
        cur = self.head
        prev = None

        while cur and pos > 0:
            prev = cur
            cur = cur.getNext()
            pos -= 1

        if pos != 0:
            return
        temp = Node(item)
        temp.setNext(cur)
        if prev == None:
            self.head = temp
        else:
            prev.setNext(temp)

    def pop(self):
        if not self.head:
            return
        
        cur = self.head
        prev = None
        while cur.getNext():
            prev = cur
            cur = cur.getNext()

        if prev == None:
            del cur
            self.head = None
        else:
            prev.setNext(None)
            del cur

    def popfrom(self, pos):

        cur = self.head
        prev = None
        while cur and pos > 0:
            prev = cur
            cur = cur.getNext()
            pos -= 1

        if pos > 0 or not cur:
            return

        if prev == None:
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext())
        del cur




if __name__ == "__main__":
    mylist = UnorderedList()
    print(f"{mylist.isEmpty()=}")
    print(f"{mylist.size()=}")

    mylist.add(31)
    print(f"{mylist.size()=}")
    mylist.add(77)
    print(f"{mylist.size()=}")
    mylist.add(17)
    print(f"{mylist.size()=}")
    mylist.add(93)
    print(f"{mylist.size()=}")
    mylist.add(26)
    print(f"{mylist.size()=}")
    mylist.add(54)
    print(f"{mylist.size()=}")
    print(f"{mylist.isEmpty()=}")

    print(f"{mylist.search(17)=}")
    print(f"{mylist.search(-1)=}")

    print(mylist)
    mylist.remove(17)
    print("After remove(17)")
    print(mylist)
    print("After remove(-1)")
    mylist.remove(-1)
    print(mylist)
    print("After remove(54)")
    mylist.remove(54)
    print(mylist)
    print("After remove(31)")
    mylist.remove(31)
    print(mylist)
    print("After remove(93)")
    mylist.remove(93)
    print(mylist)
    print("After remove(77)")
    mylist.remove(77)
    print(mylist)
    print("After remove(26)")
    mylist.remove(26)
    print(mylist)
    print("After remove(0)")
    mylist.remove(0)
    print(mylist)

    print()
    mylist.append(54)
    print("After append(54)")
    print(mylist)
    mylist.append(26)
    print("After append(26)")
    print(mylist)
    mylist.append(93)
    print("After append(93)")
    print(mylist)

    print()
    print(f"{mylist.index(54)=}")
    print(f"{mylist.index(26)=}")
    print(f"{mylist.index(93)=}")
    print(f"{mylist.index(100)=}")

    print()
    print(mylist)
    mylist.insert(0, 100)
    print("After insert(0, 100)")
    print(mylist)
    mylist.insert(1, 1000)
    print("After insert(1, 1000)")
    print(mylist)
    mylist.insert(3, 20)
    print("After insert(3, 20)")
    print(mylist)
    mylist.insert(5, 200)
    print("After insert(5, 200)")
    print(mylist)
    mylist.insert(7, 300)
    print("After insert(7, 300)")
    print(mylist)
    mylist.insert(10, 3000)
    print("After insert(10, 3000)")
    print(mylist)

    print()
    print(mylist)
    while not mylist.isEmpty():
        mylist.pop()
        print("After pop()")
        print(mylist)

    print()
    mylist.append(54)
    mylist.append(26)
    mylist.append(93)
    mylist.append(104)
    print(mylist)
    mylist.popfrom(0)
    print("After popfrom(0)")
    print(mylist)
    mylist.popfrom(1)
    print("After popfrom(1)")
    print(mylist)
    mylist.popfrom(1)
    print("After popfrom(1)")
    print(mylist)
    mylist.popfrom(0)
    print("After popfrom(0)")
    print(mylist)

    

    

    
