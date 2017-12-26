from CHAPTER2.MyLinkedList import *


# O(n^2)
def is_intersecting(ll1, ll2):

    ptr1 = ll1.head

    while ptr1 is not None:
        ptr2 = ll2.head
        while ptr2 is not None:
            if ptr1 == ptr2:
                return ptr1
            ptr2 = ptr2.next
        ptr1 = ptr1.next

    return False


#O(n) -> tradeoff is extra space
def is_intersecting_method2(ll1, ll2):

    ptr1 = ll1.head
    l1 = set()

    while ptr1 is not None:
        l1.add(ptr1)
        ptr1 = ptr1.next

    ptr2 = ll2.head

    while ptr2 is not None:
        if ptr2 in l1:
            return ptr2
        ptr2 = ptr2.next

    return False


#O(n) in place
def is_intersecting_method3(ll1, ll2):

    len1 = ll1.size()
    len2 = ll2.size()
    diff = abs(len1 - len2)

    if len1 > len2:
        first = ll1
        second = ll2
    else:
        first = ll2
        second = ll1

    # Just moving the bigger ll by difference steps , so that in the next step both lists can move together
    ptr1 = first.head

    for i in range(diff):
        ptr1 = ptr1.next

    # Now both lists can be moved together
    ptr2 = second.head

    while ptr2:
        if ptr2 == ptr1:
            return ptr2
        ptr2 = ptr2.next
        ptr1 = ptr1.next

    return False


def main():

    a = SinglyLinkedList()
    b = SinglyLinkedList()
    c = SinglyLinkedList()

    n =[]
    for x in [3, 5, 6, 0, 9, 5, 3]:
        n.append(Node(x))

    for i in range(len(n)):
        a.add_node_to_tail(n[i])

    b.add_node_to_tail(Node(1))
    b.add_node_to_tail(Node(2))

    for i in range(1,len(n)):
        b.add_node_to_tail(n[i])

    for x in [3, 5, 6, 0, 9, 5, 3]:
        c.add_node_to_tail(Node(x))

    print(is_intersecting(a, b))
    print(is_intersecting(a, c))
    print(is_intersecting_method2(a, b))
    print(is_intersecting_method3(a, b))




if __name__ == '__main__':
    main()