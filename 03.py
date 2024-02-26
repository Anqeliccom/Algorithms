arr = [1, 2, 7, 13, 35, 37, 90, 93, 99]
l = 0
r = len(arr) - 1
i = 35

def binary(l, r, i):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == i:
            return mid
        elif i < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

print(binary(l, r, i))

