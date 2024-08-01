def reverseWords(s):
    s=s.split()
    list1 = []
    
    for word in s:
        word = list(word)
        # print(word)
        left = 0
        right = len(word)-1

        while left < right:
            word[left], word[right] = word[right], word[left]
            left +=1
            right -=1
            
        word ="".join(word)
        list1.append(word)
    return " ".join(list1)

s = "Let's take LeetCode contest"
print(reverseWords(s))
s = "God Ding"
print(reverseWords(s))