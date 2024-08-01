def toLowerCase(s):
    l = []
    for ele in s:
        if ele.isupper():
            l.append(ele.lower())
        else:
            l.append(ele)
    return ''.join(l)


    # s_list = [c.lower() if c.isupper() else c for c in s]
    # return ''.join(s_list)

s='Hello'
s1 = "LOVELY"
s3 = 'here'
print(toLowerCase(s))
print(toLowerCase(s1))
print(toLowerCase(s3))