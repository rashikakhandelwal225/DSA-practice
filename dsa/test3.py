MOD = 10**9 + 7
def minNonZeroProduct(p):
    largest = pow(2, p) - 1
    secondLargest = largest - 1
    numberOfTimes =  pow(2, p - 1)- 1
    return (largest * pow(secondLargest, numberOfTimes, MOD)) % MOD

p=1
print(minNonZeroProduct(p))
p=2
print(minNonZeroProduct(p))
p=3
print(minNonZeroProduct(p))
p=45
print(minNonZeroProduct(p))