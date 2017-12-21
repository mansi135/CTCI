#is_substring & Rotated

def is_substring(str1, str2):

    for i in range(len(str1)):
        j = 0
        while j < len(str2):
            if str1[i] != str2[j]:
                break
            j += 1
            i += 1
        if j == len(str2):
            return True
        i += 1

    return False


def is_substring_method2(str1, str2):
    return str1.find(str2) > -1


def is_rotated(str1, str2):
    twicestr = str1 + str1
    if is_substring_method2(twicestr, str2) and len(str1) == len(str2):
        return "Rotated"
    else:
        return "Non-Rotated"


def main():

    print(is_rotated('waterbottle', 'tlewaterbot'))


if __name__ == "__main__":
    main()

