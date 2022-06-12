# Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
# A string is said to be a child of an another string if it can be formed by deleting 0 or more characters from the other string.
# input  => ABCD,ABDC
# longest strings formed => ABC,ABD
# output => 3


# a = [A,B,C]
# # b = [A,B,D]

# i =0
# j = 0

# ABCD  ABDC
#   i      j

def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])


def find_longest_child(str1, str2):
    n, m = len(str1), len(str2)
    lcs = [[0]*(m+1) for i in range(n+1)]
    for i, c1 in enumerate(str1):
        for j, c2 in enumerate(str2):
            if c1 == c2:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            # printGrid(lcs)
            # print()
    # print(lcs)
    return lcs[n-1][m-1]


print(find_longest_child('ABCD', 'ABDC'))
