def merge(l, r):
    li = 0
    ri = 0
    newArr = []
    while(li < len(l) and ri < len(r)):
        if(l[li] <= r[ri]):
            newArr.append(l[li])
            li += 1
        else:
            newArr.append(r[ri])
            ri += 1
    return newArr + l[li:] + r[ri:]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    # print(arr[0:mid+1], arr[mid+1:])
    l = merge_sort(arr[0:mid])
    r = merge_sort(arr[mid:])
    return merge(l, r)


arr = [10, 2, 14, 7, 9, 2]
# mid = len(arr) // 2
# print(arr[0:mid+1], arr[mid+1:])
print(merge_sort(arr))

# print(merge([2, 11],[3, 4]))
