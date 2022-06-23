# input =>
# v = 60 100 120
# w = 10 20 30
# W = 50
# output => 220


# ================================ matrix approach ==============================

val = [10, 15, 40]
wts = [1, 2, 3]
W = 6

mat = [[0 for _ in range(W+1)] for _ in range(len(val)+1)]
# print(mat)

#       0   1   2   3   4   5   6
#    0 [0,  0,  0,  0,  0,  0,  0]
# 10 1 [0, 10, 10, 10, 10, 10, 10]
# 15 2 [0, 10, 15, 25, 25, 25, 25]
# 40 3 [0, 10, 15, 40, 50, 55, 65]


for i in range(len(val)+1):
    for w in range(W + 1):
        if w == 0 or i == 0:
            mat[i][w] = 0
        elif wts[i-1] > w:
            mat[i][w] = mat[i-1][w]
        else:
            mat[i][w] = max(val[i-1] + mat[i-1][w - wts[i-1]], mat[i-1][w])

print(mat[i][w])
