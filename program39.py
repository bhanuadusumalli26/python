def sumArray(arr, n, k):
    hashmap = {}
    a = []
    sum = 0
    for i in range(n):
        sum += arr[i]
        rem = sum - k
        if rem in hashmap:
            a.append(hashmap[rem] + 1)
            a.append(i + 1)
            return a
        hashmap[sum] = i
    return a


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
k = 15
print(sumArray(arr, n, k))
# time complexity is O(n) and space complexity is O(n)
