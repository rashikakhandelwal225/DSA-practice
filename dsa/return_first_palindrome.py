def palindrome(str1):
    list1 = list(str1)
    left = 0
    right = len(list1) - 1

    while left < right:
        if list1[left] == list1[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def firstPalindrome(words):
    flag = False
    for str1 in words:
        flag = palindrome(str1)
        if flag == True:
            return str1
    return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))