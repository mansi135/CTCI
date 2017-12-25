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
    l1 = {}

    while ptr1 is not None:
        l1[ptr1] = True
        ptr1 = ptr1.next

    ptr2 = ll2.head

    while ptr2 is not None:
        if ptr2 in l1:
            return ptr2
        ptr2 = ptr2.next

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

    for i in range(4,len(n)):
        b.add_node_to_tail(n[i])

    for x in [3, 5, 6, 0, 9, 5, 3]:
        c.add_node_to_tail(Node(x))

    print(is_intersecting_method2(a, b))
    print(is_intersecting(a, b))
    print(is_intersecting(a, c))



if __name__ == '__main__':
    main()