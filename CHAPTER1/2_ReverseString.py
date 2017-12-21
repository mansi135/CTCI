# reverse string

def reverse_string(stri):
    rstr = []
    j = 0
    for i in range(len(stri)-1,-1,-1):
        rstr.append(stri[i])

    return "".join(rstr)


def reverse_string1(stri):
    rstr=''
    for i in range(len(stri)-1,-1,-1):
        rstr+=stri[i]

    return rstr


def reverse_string2(stri):
    rstr = stri[::-1]
    return rstr


def reverse_list(new_list):
    n = len(new_list)
    for i in range(n - 1, int(n /2-1), -1):
        temp = new_list[n-i-1]
        new_list[n-i-1] = new_list[i]
        new_list[i] = temp
    return new_list


def main():
    print(reverse_string('Trump is moonkey'))
    print(reverse_string1('God is magic'))
    print(reverse_string2('Pogo'))

    new_list = ['a', 'z', 'e', 'p', 'c']
    print(reverse_list(new_list))
    new_list = [1, 2, 3, 4]
    print(reverse_list(new_list))
    new_list = ['aihf', 'zojwer', 'whrl', 'pool']
    print(reverse_list(new_list))
    new_list = [4, 6, 3, 2, 9, 0, 1]
    print(reverse_list(new_list))
    new_list = []
    print(reverse_list(new_list))


if __name__ == "__main__":
    main()
