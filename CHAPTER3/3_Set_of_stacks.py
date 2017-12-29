#SetofStacks


class Stack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def peek(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.stack[len(self.stack)-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.stack.pop()


class SetOfStacks:

    capacity = 3

    def __init__(self):
        self.stacks_full = []
        self.stack_current = Stack(SetOfStacks.capacity)

    def push(self, data):
        if self.stack_current.is_full():
            self.stacks_full.append(self.stack_current)
            self.stack_current = Stack(SetOfStacks.capacity)
        self.stack_current.push(data)

    def is_empty(self):
        return self.stack_current.is_empty() and len(self.stacks_full) == 0

    # peek should not modify
    def peek(self):
        return self.stack_current.peek()

    # The invariant here is that current stack should always point to a valid top value
    def pop(self):
        p = self.stack_current.pop()
        if self.stack_current.is_empty() and len(self.stacks_full) != 0:
            self.stack_current = self.stacks_full.pop()
        return p


def main():
    s = SetOfStacks()
    s.push(3)
    s.push(5)
    s.push(14)
    s.push(2)
    s.push(4)
    s.push(1)
    s.push(1)
    s.push(1)
    print(s.stacks_full)
    print(s.peek())

    s.pop()
    s.pop()
    print(s.stacks_full)

    s.pop()
    print(s.stacks_full)

    print(s.peek())
    s.pop()
    s.pop()

    print(s.peek())
    print(s.stacks_full)
    s.pop()
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())


if __name__ == "__main__":
    main()
