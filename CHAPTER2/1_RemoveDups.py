from CHAPTER2.MyLinkedList import SinglyLinkedList


def remove_duplicates(a):

    if a.head == None:  # Empty LL
        return

    list1 = [a.head.data]

    n = a.head
    while n.next != None:
        if n.next.data not in list1:
            list1.append(n.next.data)
            n = n.next
        else:
            n1 = n.next
            while n1.data in list1:
                n1 = n1.next
                if n1 == None:
                    break
            n.next = n1

    return a


def remove_duplicates_method2(a):

    if a.head == None:  # Empty LL
        return

    list1 = [a.head.data]

    n = a.head
    while n.next:
        if n.next.data in list1:
            n.next = n.next.next
        else:
            list1.append(n.next.data)
            n = n.next
    return a


def remove_duplicates_followup(a):

    if a.head == None:  # Empty LL
        return


    # Think of it like nested for loop O(n^2)
    # As soon as we find a number equal to current outer for loop, remove it
    ptr1 = a.head
    while ptr1.next != None:
        ptr2 = ptr1
        while ptr2.next != None:
            if ptr2.next.data == ptr1.data:
                ptr2.next = ptr2.next.next
            else:
                ptr2 = ptr2.next
        ptr1 = ptr1.next

    return a





def main():

    a = SinglyLinkedList()

    a.add_to_tail(6)
    a.add_to_tail(1)
    a.add_to_tail(1)
    a.add_to_tail(2)
    a.add_to_tail(3)
    a.add_to_tail(4)
    a.add_to_tail(4)
    a.add_to_tail(5)
    a.add_to_tail(2)
    a.add_to_tail(3)
    remove_duplicates(a).print()
    print("\n")
    remove_duplicates_method2(a).print()
    print("\n")
    remove_duplicates_followup(a).print()


if __name__ == '__main__':
    main()