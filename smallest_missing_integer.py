# find the smallest missing +ve integer in array
# input  => [-6,2,4,1,5,-2,3]
# output => 6

# time complexity = O(n)
# space complexity = O(1) extra space

def find_smallest(arr):
    d = {}

    # this will take o(n)
    for ele in arr:
        if ele > 0:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1

    # this will take o(n)
    for i in range(1, 2000000):
        if i not in d.keys():
            return i


arr = [-6, 2, 4, 1, 5, -2, 3]
# print(find_smallest(arr))

# ================================== efficient way ===============================

# time complexity = O(n)
# space complexity = O(1) extra space

arr = [-5, 4, 2, -4, 8, -3, 9, -1, 1, 0]


def separateNegatives(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] <= 0:
            i += 1
        elif arr[j] > 0:
            j -= 1
        elif arr[i] > 0 and arr[j] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
    return i


def find_missing(arr):
    for i in range(len(arr)):
        if abs(arr[i]) - 1 < len(arr) and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    print(arr)

    for i in range(len(arr)):
        if arr[i] > 0:
            return i + 1


def smallest_missing_efficient(arr):
    positiveInd = separateNegatives(arr)
    print(arr[positiveInd:])
    return find_missing(arr[positiveInd:])


# print(separateNegatives(arr))
print(smallest_missing_efficient(arr))
