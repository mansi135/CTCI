# Perform push , pop and min operation on a stack in constant time
# Approach is to maintain one more stack which always has the smallest value at the top
# Hence accessing top of stack is always O(1)
# Remember - whenever trying to improve time complexity, space has to be compromised . That's a trade-off
# Here I increased space in the form of stack


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.stack[len(self.stack)-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.stack.pop()


class StackMin:

    def __init__(self):
        self.stack_of_values = Stack()
        self.stack_min = Stack()

    def push(self, data):
        self.stack_of_values.push(data)
        if self.stack_min.is_empty() or data <= self.stack_min.peek():
            self.stack_min.push(data)

    def is_empty(self):
        return self.stack_of_values.is_empty()

    def peek(self):
        return self.stack_of_values.peek()

    def pop(self):
        p = self.stack_of_values.pop()
        if p == self.stack_min.peek():
            self.stack_min.pop()
        return p

    def min(self):
        if self.stack_min.is_empty():
            raise Exception('Empty Stack')
        return self.stack_min.peek()


def main():
    s = StackMin()
    s.push(3)
    s.push(5)
    s.push(4)
    s.push(2)
    s.push(4)
    print("The current minimum element is  ", s.min())
    s.pop()
    print("The current minimum element is  ", s.min())
    s.pop()
    print("The current minimum element is  ", s.min())
    s.push(1)
    s.push(1)
    s.push(1)
    print("The current minimum element is  ", s.min())
    s.pop()
    s.pop()
    print("The current minimum element is  ", s.min())
    print(s.peek())


if __name__ == "__main__":
    main()
