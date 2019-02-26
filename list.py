class List:
    head = tail = None

    def __init__(self, value=None, next_=None):
        if value is not None:
            self.append(value)
        if next_ is not None:
            self.append(value)

    def append(self, data=None):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print(self):
        p = self.head
        while p is not None:
            p.Print()
            p = p.next


class Node:
    data = None
    next = None
    def __init__(self, data=None):
        self.data = data
    def Print(self):
        print(self.data)

list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
list_.print() # output: 1 2 3