
class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self,value):
        node = Node(value)
        self.add_node_to_head(node)

    def add_node_to_head(self, n):
        self.count += 1
        if self.tail is None:
            self.tail = n
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def add_to_tail(self,value):
        node = Node(value)
        self.add_node_to_tail(node)

    def add_node_to_tail(self, n):
        self.count += 1
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def remove_node_from_head(self):
        if self.is_empty():
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            temp.next = None        # While removing node, remember to set its next pointer to None
        self.count -= 1
        return temp

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next




# In Doubly LL, I am overriding str method
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self,value):
        n = Node(value)
        self.count += 1
        if self.tail is None:
            self.tail = n
            self.head = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def add_to_tail(self,value):
        n = Node(value)
        self.count += 1
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def remove_node_from_head(self):
        if self.is_empty():
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
            temp.next = None
        self.count -= 1
        return temp

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def to_list(self):
        l = []
        temp = self.head
        while temp:
            l.append(temp.data)
            temp = temp.next
        return l

    def __str__(self):
        return str(self.to_list())


