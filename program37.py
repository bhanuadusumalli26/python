# Optimal Approach
def frequency(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])
    print(mp)


arr = [1, 2, 3, 2, 3, 5, 5]
n = len(arr)
frequency(arr, n)
