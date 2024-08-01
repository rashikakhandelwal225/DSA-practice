def min_operations(n, m, a, b):
    # Sort the arrays a and b
    a.sort()
    b.sort(reverse=True)

    # Initialize the number of operations
    operations = 0

    # Iterate through the arrays to satisfy the condition
    for i in range(min(n, m)):
        if a[i] < b[i]:
            # Perform operations to make a[i] at least as large as b[i]
            operations += b[i] - a[i]

    return operations

n1, m1 = 2, 2
a1 = [2, 3]
b1 = [3, 5]
result1 = min_operations(n1, m1, a1, b1)
print(result1)

n2, m2 = 3, 2
a2 = [4, 5, 6]
b2 = [1, 2]
result2 = min_operations(n2, m2, a2, b2)
print(result2)