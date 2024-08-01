def kWeakestRows(matrix, k):


#     row_strength = [(sum(row), i) for i, row in enumerate(matrix)]
#     print(row_strength)
#     row_strength.sort()
#     print(row_strength)
#
#     result = [row[1] for row in row_strength[:k]]
#     return result
#
# # Example usage:
matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
#
output = kWeakestRows(matrix, k)
print(output)
