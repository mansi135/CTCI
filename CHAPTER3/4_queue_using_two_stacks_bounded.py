# Not a preferred way to import since module name should not start with numeral

from importlib import import_module
mystack = import_module('3_Set_of_stacks')


class MyQueue:

    def __init__(self):
        self.stack_enq = mystack.Stack(3)
        self.stack_deq = mystack.Stack(3)

    def enqueue(self, data):
        if self.stack_enq.is_full():
            if self.stack_deq.is_full():
                raise Exception('Queue full')
            if self.stack_deq.is_empty():
                self.drain_1to2()
            else:
                raise Exception('Please wait for dequeue stack to be empty')

        self.stack_enq.push(data)


    def dequeue(self):
        if self.stack_deq.is_empty():
            if self.stack_enq.is_empty():
                raise Exception('Queue empty')
            else:
                self.drain_1to2()

        return self.stack_deq.pop()


    def drain_1to2(self):
        while not self.stack_enq.is_empty():
            self.stack_deq.push(self.stack_enq.pop())


    #def is_empty(self):

    #def peek(self):


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
    q.dequeue()
    q.dequeue()
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

if __name__ == "__main__":
    main()


