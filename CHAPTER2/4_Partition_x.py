# Partition linked-list around x .

from CHAPTER2.MyLinkedList import *


# I make a new linked list , which has add-to-head and add-to-tail methods .
# If num is < x, I add to head, else I add to tail
# then return new_ll
def partition(ll, x):

    new_ll = SinglyLinkedList()

    node = ll.head
    while node:
        if node.data < x:
            new_ll.add_to_head(node.data)
        else:
            new_ll.add_to_tail(node.data)
        node = node.next

    return new_ll



# In this method, i make 3 separate LL for smaller, equal and bigger and then concatenate and return
def partition_method2(ll, x):

    equal = SinglyLinkedList()
    smaller = SinglyLinkedList()
    bigger = SinglyLinkedList()

    start = ll.head

    while start is not None:
        if start.data == x:
            equal.add_to_tail(x)
        elif start.data < x:
            smaller.add_to_tail(start.data)
        else:
            bigger.add_to_tail(start.data)
        start = start.next

    if smaller.tail:
        smaller.tail.next = equal.head

    if equal.tail:
        equal.tail.next = bigger.head

    if smaller.head:
        return smaller

    if equal.head:
        return equal

    if bigger.head:
        return bigger



def main():

    a = SinglyLinkedList()

    a.add_to_tail(3)
    a.add_to_tail(5)
    a.add_to_tail(8)
    a.add_to_tail(5)
    a.add_to_tail(10)
    a.add_to_tail(2)
    a.add_to_tail(4)

    a = partition(a, 5)
    a.print()

    a = partition_method2(a, 8)
    a.print()



if __name__ == '__main__':
    main()