def sort012(arr, n):
    # Perform merge sort on the array
    mergeSort(arr, 0, n - 1)
    return arr


def mergeSort(arr, left, right):
    if left < right:
        # Find the middle point
        mid = (left + right) // 2

        # Recursively sort first and second halves
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    # Sizes of the two subarrays to be merged
    n1 = mid - left + 1
    n2 = right - mid

    # Temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[left..right]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Example usage
arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
n = len(arr)
sort012(arr, n)
print(arr)
# timecomplexity O(nlogn)
# spacecomplexity O(n)
