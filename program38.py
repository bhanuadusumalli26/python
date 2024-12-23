# pair of two elements in array  equals to given sum
def sumArray(arr, n, sum):
    a = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                a.append([i, j])
    return a[0] if a else [-1, -1]


arr = [1, 2, 3, 4, 5]
n = len(arr)
sum = 10
print(sumArray(arr, n, sum))
# Time complexity: O(n^2)
# Space complexity: O(1)
