def isAnagram(self, s: str, t: str) -> bool:
    s = "anagram"
    t = "nagaram"
    uniqueChar_s= set(s)  #//{r, m , g , n , a}
    uniqueChar_t = set(t) 
    if set(s) == set(t):
        flag_unique = true
    else:
        flag_unique = false
        
    if flag_unique == true:
        for i in range(0, len(uniqueChar_s)):
            count = 0
            if uniqueChar_s[i] in s[::]:
                count += 1
        
# if count(a) in s == count(a) in t: