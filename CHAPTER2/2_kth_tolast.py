# Kth to the last of a SinglyLinkedList

from CHAPTER2.MyLinkedList import SinglyLinkedList

# if n-k == diff :
#     k starts moving
#   else:
#     n keeps on moving
# The intention is to keep the distance constant between n and k

def kth_to_last(ll, kth):

    if ll.head is None:
        return "Linked List is empty"

    n = 0
    k = 0
    ptr1 = ptr2 = ll.head

    while ptr2.next is not None:
        if n - k == kth - 1:
            ptr1 = ptr1.next
            k += 1
        ptr2 = ptr2.next
        n += 1

    if kth-1 > n :
        return "kth is greater than Linked List size"

    return ptr1.data


def kth_to_last_method2(ll, kth):

    if ll.head is None:
        return "Linked List is empty"

    ptr1 = ptr2 = ll.head
    for i in range(kth):
        if ptr2:
            ptr2 = ptr2.next
        else:
            return "kth is greater than Linked List size"


    while ptr2 is not None:
        ptr2 = ptr2.next
        ptr1 = ptr1.next

    return ptr1.data


def main():

    a = SinglyLinkedList()

    a.add_to_tail(6)
    a.add_to_tail(1)
    a.add_to_tail(22)
    a.add_to_tail(3)
    a.add_to_tail(4)
    a.add_to_tail(147)
    a.add_to_tail(5)
    a.add_to_tail(20)
    a.add_to_tail(39)

    b = SinglyLinkedList()

    #print(kth_to_last(a, 1))
    #print(kth_to_last(b, 1))

    print(kth_to_last_method2(a, 10))
    print(kth_to_last_method2(b, 1))


if __name__ == '__main__':
    main()