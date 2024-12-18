def frequencyArr(arr):
    # To keep track of already processed elements
    processed = set()

    for i in range(len(arr)):
        # If the element is already counted, skip it
        if arr[i] in processed:
            continue

        count = 0
        # Count occurrences of arr[i]
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        # Mark this element as processed
        processed.add(arr[i])

        # Print the element and its count
        print(arr[i], count)


# Example usage
arr = [1, 2, 3, 2, 3]
frequencyArr(arr)
