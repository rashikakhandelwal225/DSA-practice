def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
        # in-place means we are solving without copying , we are saving the extra memory of copy.

        #Using swaping of two left and right pointers
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1

    return s

s = ["h","e","l","l","o"]
print(reverseString(s))
s = ["H","a","n","n","a","h"]
print(reverseString(s))