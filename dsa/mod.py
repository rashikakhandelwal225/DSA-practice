def mod(a):
    result = 1
# Calculate the product
    for num in a:
        result = (result * num) % (10**9 + 7)

    return result

a = [5, 3, 7, 2]
print(mod(a))
a = [1,2,3,4,5,6,7]
print(mod(a))

