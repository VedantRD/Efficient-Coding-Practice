# Given an array with repeated elements, find the maximum distance between two occurrences of all the elements in the array.
# input =>  [3,2,1,2,1,4,5,8,6,7,4,2,10]
# output => 10

def find_maximum_distance(arr):
    maxD = 0
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d.keys():
            d[arr[i]] = i
        else:
            maxD = max(maxD, i - d[arr[i]])

    return maxD

arr = [3,2,1,2,1,4,5,8,6,7,4,2,10]
print(find_maximum_distance(arr))