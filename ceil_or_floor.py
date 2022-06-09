# given an sorted array of integers. n will be given fin the ceil of n from array
# arr = [2,3,6,9,10]
# input  => 4
# output => 6
# input  => 9
# output => 9

def find_ceil(arr,low,high,n):
    
    if n < arr[low]:
        return low
    
    mid = (low + high) // 2
    if n == arr[mid]:
        return mid

    elif n > arr[mid]:
        if mid + 1 <= high and n <= arr[mid+1]:
            return mid + 1
        else:
            return find_ceil(arr,mid+1,high,n)
    else:
        return find_ceil(arr,low,mid-1,n)


arr = [2,3,6,9,10]
n = 11

if n > arr[-1]:
    print(n)
else:
    ind = find_ceil(arr,0,len(arr)-1,n)
    print(arr[ind])

# print()
