# Replace spaces with %20

def replace(stri, length):
    s = list(stri)
    extra = 0
    j = 0
    for i in range(length):
        if s[i] == ' ':
            extra += 2

    for i in range(length+extra):
        if s[i] == ' ':
            temp = s[i + 1:length + 2 * j:1]
            s[i] = '%'
            s[i + 1] = '2'
            s[i + 2] = '0'
            s = s[0:i + 3] + temp
            i += 3
            j += 1

    return "".join(s)

print(replace('Being rich is a joke          ', 20))