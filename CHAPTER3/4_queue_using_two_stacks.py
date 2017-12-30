# This is an unbounded queue version

from importlib import import_module
mystack = import_module('3_Set_of_stacks')


class MyQueue:

    def __init__(self):
        self.stack_enq = mystack.Stack(-1)
        self.stack_deq = mystack.Stack(-1)

    def enqueue(self, data):
        self.stack_enq.push(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue empty')

        elif self.stack_deq.is_empty():
            self.drain_1to2()

        return self.stack_deq.pop()

    def drain_1to2(self):
        while not self.stack_enq.is_empty():
            self.stack_deq.push(self.stack_enq.pop())

    def is_empty(self):
        return self.stack_enq.is_empty() and self.stack_deq.is_empty()

    def peek(self):
        if self.is_empty():
            raise Exception('Queue empty')

        elif self.stack_deq.is_empty():
            self.drain_1to2()

        return self.stack_deq.peek()



def main():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.stack_enq)
    print(q.stack_deq)
    q.enqueue(4)
    print(q.stack_enq)
    print(q.stack_deq)
    print(q.dequeue())
    print(q.dequeue())
    print(q.stack_enq)
    print(q.stack_deq)
    q.dequeue()
    print(q.stack_enq)
    print(q.stack_deq)
    q.enqueue(9)
    q.dequeue()
    print(q.stack_enq)
    print(q.stack_deq)
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.dequeue()
    print(q.stack_enq)
    print(q.stack_deq)
    q.enqueue(88)
    print(q.peek())
    print(q.stack_enq)
    print(q.stack_deq)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.stack_enq)
    print(q.stack_deq)
    print(q.peek())
    print(q.stack_enq)
    print(q.stack_deq)

if __name__ == "__main__":
    main()


