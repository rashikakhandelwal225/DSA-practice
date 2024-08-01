def totalElements(N, arr):
    size = 0  # Size of the largest subarray with at most two distinct elements

    # Generate all subarrays
    for i in range(N):
        for j in range(i, N):
            # Create a set to store distinct elements
            distinct = set()

            # Check if the subarray has at most two distinct elements
            for k in range(i, j + 1):
                distinct.add(arr[k])
                if len(distinct) > 2:
                    break

            # Update the size of the largest subarray
            if len(distinct) <= 2:
                size = max(size, j - i + 1)

    return size


# Driver code
if __name__ == "__main__":
    N = 6
    arr = [0, 1, 2, 2, 2, 2]

    # Function call
    ans = totalElements(N, arr)
    print(ans)