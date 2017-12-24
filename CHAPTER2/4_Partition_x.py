# Partition linked-list around x .
# I make a new linked list , which has add-to-head and add-to-tail methods .
# If num is < x, I add to head, else I add to tail
# then return new_ll

from CHAPTER2.MyLinkedList import *


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




if __name__ == '__main__':
    main()