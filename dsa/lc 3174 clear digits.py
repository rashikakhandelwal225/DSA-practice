def clearDigits(s):
    for ch in s:
        if ch.isdigit() == True:
            i = s.index(ch)
            s= s.replace(s[i], '',1)
            print(s[i-1])
            print(s.index('c'))
            s= s.replace(s[i-1], '', 1)

    return s

# s = "cb34"
# print(clearDigits(s))
#
# s = "cbfg34"
# print(clearDigits(s))

s= 'c5k5'
print(clearDigits(s))

s= "gbysb5"
