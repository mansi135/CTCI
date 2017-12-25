from CHAPTER2.MyLinkedList import *

def is_palindrome(ll):
    start = ll.head
    end = ll.tail

    while start != end:

        if start.data != end.data:
            return False
        if start.next == end:
            return True
        start = start.next
        end = end.prev

    return True



def main():

    a = DoublyLinkedList()

    for x in [3, 5, 6, 0, 9, 5, 3]:
        a.add_to_tail(x)

    print(is_palindrome(a))

if __name__ == '__main__':
    main()