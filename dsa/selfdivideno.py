def selfDividingNumbers(left, right):
    l1 = []
    while left <= right:
        flag = True
        num = left
        for j in str(num):
            if j !='0':
                if num % int(j) != 0 :
                    flag = False
            else:
                flag = False
                break
            
        if flag:
            l1.append(num)
            
        left +=1
        
    return l1

left = 1
right = 22
print(selfDividingNumbers(left, right))
left = 47
right = 85
print(selfDividingNumbers(left, right))