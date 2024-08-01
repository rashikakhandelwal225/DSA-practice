def maxScore(cardPoints, k):
    max_score = 0
    n = len(cardPoints)
    i = 0
    right = n-1


    #sum of 1st k elements
    left_sum = 0
    right_sum = 0
    while i <= k-1:
        left_sum += cardPoints[i]
        i+=1
    max_score = left_sum

#i reached to k-1
    for i in range(k-1, -1, -1):
        left_sum -= cardPoints[i]
        right_sum += cardPoints[right]
        right -=1

        max_score = max(max_score, left_sum+right_sum)
    return max_score





# cardPoints =[11,49,100,20,86,29,72]
# k=4
# print(maxScore(cardPoints, k))
# cardPoints =[100,40,17,9,73,75]
# k= 3
# print(maxScore(cardPoints, k))
# cardPoints = [1,79,80,1,1,1,200,1]
# k=3
# print(maxScore(cardPoints, k))
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxScore(cardPoints, k))
# cardPoints = [9,7,7,9,7,7,9]
# k = 7
# print(maxScore(cardPoints, k))