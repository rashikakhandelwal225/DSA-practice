from collections import Counter
def counter(hashmap, count):
    if 'a' in hashmap and 'b' in hashmap and 'c' in hashmap:
        if hashmap['b'] > hashmap['a'] and hashmap['c'] > hashmap['a']:
            count += 1
        elif hashmap['b'] < hashmap['a'] and hashmap['c'] < hashmap['a']:
            count += 1
        elif hashmap['b'] > hashmap['a'] and hashmap['b'] > hashmap['c']:
            count += 1
        elif hashmap['c'] > hashmap['a'] and hashmap['c'] > hashmap['b']:
            count += 1
    else:
        count = 0
    return count


def numberOfSubstrings(s):
    hashmap = {}
    count = 0
    global_count = 0
    remaining_chars = 0
    j = 0

    while j in range(len(s)):
        for i in range(j, len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
                count=counter(hashmap, count)
            else:
                if 'a' in hashmap and 'b' in hashmap and 'c' in hashmap:
                    if s[i] == 'a':
                        count +=1
                    elif s[i] == 'b':
                        count +=1
                    elif s[i] == 'c':
                        count +=1
        j += 1
        global_count += count
        hashmap = {}

    return global_count

s = "abc"
print(numberOfSubstrings(s))

s = "aaacb"
print(numberOfSubstrings(s))
s=  "abcabc"
print(numberOfSubstrings(s))
