def canDivideChocolate(n):
    c1 = (n//2)
    if c1 %2 == 0:
        c1 -=1
    print(c1)
    c2 = n-c1
    print(c2)
    r1 = isOdd(c1)
    r2 = isOdd(c2)

    if r1 == 1 and r2==1:
        print("YES")
    else:
        print('NO')


def isOdd(num):
    if num>0 and num%2 == 1:
        return 1


canDivideChocolate(18)