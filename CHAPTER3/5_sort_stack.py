# Sort a stack in ascending order using a temporary stack


from importlib import import_module
mystack = import_module('3_Set_of_stacks')


def sort(stack):

    temp_stack = mystack.Stack(-1)


    while not stack.is_empty():
        minstack = stack.pop()
        if temp_stack.is_empty() or temp_stack.peek() < minstack:
            temp_stack.push(minstack)
        else:
            while temp_stack.peek() > minstack:
                stack.push(temp_stack.pop())
                if temp_stack.is_empty():
                    break
            temp_stack.push(minstack)

    print(temp_stack)

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





# A more verbose algorithm

# def sort(stack):
#
#     temp_stack = mystack.Stack(-1)
#
#
#     while not stack.is_empty():
#         minstack = stack.pop()
#         if temp_stack.is_empty():
#             temp_stack.push(minstack)
#         else:
#             peek_temp = temp_stack.peek()
#             if peek_temp < minstack:
#                 temp_stack.push(minstack)
#             else:
#                 while peek_temp > minstack:
#                     stack.push(temp_stack.pop())
#                     if not temp_stack.is_empty():
#                         peek_temp = temp_stack.peek()
#                     else:
#                         break
#                 temp_stack.push(minstack)
#
#     print(temp_stack)
