# longest common subsequent algorithm
# Dynamic Programming Approach


def longest_common_subsequent(x, y):

    m = len(x)  # Get the length of the first word or base word
    n = len(y)  # Get the length of the second word or comparing word

    # MAKE A 2D LIST (MATRIX)
    loc = [[None] * (m + 1) for i in range(n + 1)]

    # n = NUMBER OF ROWS
    # m = NUMBER OF COLUMNS

    # MAKE THE 1ST ROW AND COLUMN FILL WITH ALL 0's.
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                loc[i][j] = 0

    # FILL THE MATRIX FOLLOWING LCS ALGORITHM.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[j - 1] == y[i - 1]:
                loc[i][j] = 1 + int(loc[i - 1][j - 1])

            else:
                loc[i][j] = max(loc[i - 1][j], loc[i][j - 1])

    print("MATRIX ACCORDING TO LONGEST COMMON SUBSEQUENT ALGORITHM: \n ")

    for i in range(n + 1):
        print(loc[i])

    print("\n\n")
    print("LENGTH OF LONGEST COMMON SUBSEQUENT = ", loc[n][m])
    print("\n\n")

    i = len(y)
    j = len(x)
    lcs = ""

    # BACKTRACKING TO FIND THE LONGEST COMMON SUBSEQUENT

    temp = True

    while temp is True:
        if loc[i][j] == 0:
            temp = False
        elif loc[i][j] == loc[i][j - 1]:
            j = j - 1

        else:
            lcs = x[j-1] + lcs
            i = i - 1
            j = j - 1

    return lcs


def main():
    x = "longest"  # x = MAIN WORD
    y = "stone"  # y = COMPARING WORD

    # CALLING THE FUNCTION
    print("THE LCS WORD IS: ", longest_common_subsequent(x, y))


if __name__ == '__main__':
    print("LONGEST COMMON SUBSEQUENT ALGORITHM CODE IMPLEMENTATION \n")
    main()
