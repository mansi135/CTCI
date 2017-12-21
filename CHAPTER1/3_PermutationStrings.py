# Check if two strings are permutations of each other
# Such strings are called Anagrams

def ana(str1, str2):
    if sorted(str1) == sorted(str2):
        print("anagram")
    else:
        print("no not")



def anagram_method2(str1, str2):

    if len(str1) != len(str2):
        return False

    count = {}
    for letter in str1:
        count[letter] = count.get(letter, 0) + 1

    for letter in str2:
        if letter not in count or count[letter] == 0:
            return False
        count[letter] -= 1

    return True



def main():
    ana("mansi", "insami")
    print(anagram_method2('345', '435'))


if __name__ == "__main__":
    main()
