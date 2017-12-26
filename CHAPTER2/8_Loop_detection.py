from CHAPTER2.MyLinkedList import *

#O(n) -> tradeoff is extra space
def is_loop_detected(ll1):

    ptr1 = ll1.head
    seen = set()

    while ptr1 is not None:
        if ptr1 not in seen:
            seen.add(ptr1)
        else:
            return ptr1
        ptr1 = ptr1.next

    return None


def main():

    a = SinglyLinkedList()

    n = []
    for x in [3, 5, 6, 0, 9, 5, 13]:
        n.append(Node(x))

    for i in range(len(n)):
        a.add_node_to_tail(n[i])

    a.add_node_to_tail(n[0])

    print(is_loop_detected(a))


if __name__ == '__main__':
    main()