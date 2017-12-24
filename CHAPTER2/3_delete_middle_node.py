#Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node.

# We can copy the data from the next node to the node to be deleted and
#  delete the next node.

from CHAPTER2.MyLinkedList import *


def delete_middle(node):

    if node.next is not None:
        node.data = node.next.data
        node.next = node.next.next
    # Following code wont work because we are reassigning and then its call by value, hence changes are not reflected back
    # else:
    #     node = None


def main():

    a = SinglyLinkedList()

    a.add_to_tail(1)
    a.add_to_tail(2)
    a.add_to_tail(3)
    a.add_to_tail(4)
    a.add_to_tail(5)

    delete_middle(a.head.next.next)

    a.print()


if __name__ == '__main__':
    main()

