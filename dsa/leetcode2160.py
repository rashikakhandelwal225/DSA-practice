def minimumSum(num):
    num = sorted(str(num))
    return int(num[0] + num[2]) + int(num[1] + num[3])

num = 2932
print(minimumSum(num))
num = 4009
print(minimumSum(num))
