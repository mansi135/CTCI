# Check if a string has all unique characters
# uniq characters word is also called isogram

def uniq_characters(str):
    s = set(str)
    if len(s) == len(str):
        return True
    else :
        return False



def uniq_characters_method2(str):
    for i in range(len(str)):
        slice = str[0:i]
        if str[i] in slice:
            return False

    return True


# Assuming Ascii characters
def uniq_characters_bit(str):
    charac = 0
    for i in range(len(str)):
        val = 1 << (ord(str[i]) - ord('a'))

        if charac & val > 0:
            return False
        charac |= val

    return True


def main():

    print(uniq_characters('fop'))
    print(uniq_characters_method2('pointsy'))
    print(uniq_characters_bit('pointss'))


if __name__ == "__main__":
	main()
