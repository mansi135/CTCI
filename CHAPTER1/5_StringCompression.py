#String Compression


def string_compress(str1):

    if len(str1) == 0:
        return str1

    compressed = [str1[0]]
    count = 1

    for i in range(1, len(str1), 1):
        if str1[i] == str1[i - 1]:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(str1[i])
            count = 1

    compressed.append(str(count))

    return min(str1, ''.join(compressed), key=len)


def main():

    print("Compressed String is : {}".format(string_compress('aabbbbbbddaaa')))
    print("Compressed String is : {}".format(string_compress('aabb')))
    print("Compressed String is : {}".format(string_compress('aabbb')))



if __name__ == "__main__":
    main()