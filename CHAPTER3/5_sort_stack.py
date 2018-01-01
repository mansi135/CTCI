# Sort a stack in ascending order using a temporary stack


from importlib import import_module
mystack = import_module('3_Set_of_stacks')


def sort(stack):

    temp_stack = mystack.Stack(-1)

    while not stack.is_empty():
        current_min = stack.pop()
        if temp_stack.is_empty() or temp_stack.peek() < current_min:
            temp_stack.push(current_min)
        else:
            while not temp_stack.is_empty() and temp_stack.peek() > current_min:
                stack.push(temp_stack.pop())
            temp_stack.push(current_min)

    # transfer temp_stack back to original stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack



def main():

    stack = mystack.Stack(-1)
    stack.push(0)
    stack.push(2)
    stack.push(7)
    stack.push(6)
    stack.push(1)
    stack.push(4)

    print(stack)

    print(sort(stack))



if __name__ == '__main__':
    main()


