
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
       # self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        n = Node(value)
        if self.tail == None:
            self.tail = n
            self.head = n
        else:
          #  self.head.prev = n
            n.next = self.head
            self.head = n

    def add_to_tail(self,value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    # remove
    # size
