def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


arr = [0, 2, 1, 2, 0]
n = len(arr)
print(sort012(arr, n))
# Time Complexity: O(n)
# Space Complexity: O(1)
