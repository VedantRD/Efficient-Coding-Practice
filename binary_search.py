def binary_search(arr, low, high, key):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, low, mid-1, key)
        else:
            return binary_search(arr, mid+1, high, key)


arr = [2, 5, 6, 8, 9, 12]
key = 7
print(binary_search(arr, 0, len(arr)-1, key))
