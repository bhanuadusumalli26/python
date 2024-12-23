def arraysum(arr, n, sum):
    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == sum:
            return [left, right]
        elif arr[left] + arr[right] < sum:
            left += 1
        else:
            right -= 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
sum = 15
print(arraysum(arr, n, sum))
# timecomplexity is O(n) and spacecomplexity is O(1)
