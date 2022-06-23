# find the maximum sum of non adjacent pairs of array elements
# arr = [3,2,7,10]
# possible combinations = (3,7), (3,10), (2,10), (7,3), (10,3), (10,2)
# output = 13

# time complexity = O(n)
# space complexity = O(n) extra space

def find_max_sum(arr):
    maxSumArr = []
    for i in range(len(arr)):
        if i == 0:
            maxSumArr.append(arr[i])
        elif i == 1:
            if arr[i] < maxSumArr[-1]:
                maxSumArr.append(arr[i-1])
            else:
                maxSumArr.append(arr[i])
        elif arr[i] + maxSumArr[i-2] > maxSumArr[-1]:
            maxSumArr.append(arr[i] + maxSumArr[i-2])
        else:
            maxSumArr.append(maxSumArr[-1])
    return maxSumArr[-1]


# ============================== efficient code ========================

# time complexity = O(n)
# space complexity = O(1) extra space

def find_max_sum_efficient(arr):

    # previousMaxSum = 0
    # currentMaxSum = 0

    # for i in arr:
    #     newPreviousMaxtSum = currentMaxSum if currentMaxSum > previousMaxSum else previousMaxSum
    #     currentMaxSum = i + previousMaxSum
    #     previousMaxSum = newPreviousMaxtSum
    # return currentMaxSum

    if len(arr) == 1:
        return arr[0]

    prevMax = arr[0]
    currMax = max(arr[0], arr[1])
    for ele in arr[2:len(arr)]:
        temp = max(currMax, prevMax + ele)
        prevMax = currMax
        currMax = temp

    return currMax


# arr = [3,2,7,10]
# arr = [-2, 1, 3, -4, 5]
arr = [3, 4, 7, 11, 15, 33, 20, 500, 777, 30, 860, 91, 44, 8462, 4888]
# print(find_max_sum(arr))
print(find_max_sum_efficient(arr))
