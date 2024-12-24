def sort012(a, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == 0:
            cnt0 += 1
        elif a[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    for i in range(cnt0):
        a[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        a[i] = 1
    for i in range(cnt0 + cnt1, n):
        a[i] = 2
    return a


a = [0, 1, 2, 0, 1, 2]
n = len(a)
print(sort012(a, n))
# Timecomplexity: O(N) + O(N)
# Space Complexity: O(1)
