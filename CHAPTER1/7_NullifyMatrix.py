# MxN matrix zero out

def matrix_zero(a):

    m = len(a)
    n = len(a[0])

    rows = [0] * m
    cols = [0] * n

    for r in range(m):
        for c in range(n):
            if a[r][c] == 0:
                rows[r] = 1
                cols[c] = 1

    for r in range(m):
        for c in range(n):
            if rows[r] == 1 or cols[c] == 1:
                a[r][c] = 0


    return a

def main():

    print(matrix_zero([
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [1, 2, 3, 4, 15],
                [16, 0, 8, 9, 20],
                [54, 64, 74, 88, 92]
            ]))


if __name__ == "__main__":
    main()