n = 3
arr = [1, 2, 3]
# output = > [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]


def permutation(arr):
    ans = []
    freq = [0]*len(arr)
    stack = []
    recurPermutation(arr, freq, stack, ans)
    # print(newAns)
    return ans


def recurPermutation(arr, freq, stack, ans):
    if len(stack) == len(arr):
        ans.append(list(stack))

    for i in range(len(arr)):
        if freq[i] == 0:
            freq[i] = 1
            stack.append(arr[i])
            recurPermutation(arr, freq, stack, ans)
            freq[i] = 0
            stack.pop()


p = permutation(arr)
print('total permutations =', len(p))
for i in range(len(p)):
    print(p[i])
