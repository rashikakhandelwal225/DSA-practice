def minNonZeroProduct(p):
    N = pow(10, 9) + 7
    max = pow(2, p) - 1
    power = pow(max - 1, ((max - 1) // 2))
    power = ((power % N) * (max % N)) % N
    return int(power)

p=1
print(minNonZeroProduct(p))
p=2
print(minNonZeroProduct(p))
p=3
print(minNonZeroProduct(p))
p=5
print(minNonZeroProduct(p))
p=45
print(minNonZeroProduct(p))
p=22
print(minNonZeroProduct(p))