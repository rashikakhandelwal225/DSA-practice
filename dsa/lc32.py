
def longestValidParentheses(s):
    st = []
    ch_count = 0
    max_count = 0
    for ch in s:
        if isOpening(ch):
            if len(st) > 0:
                ch_count = 0
            st.append(ch)

        else:
            if len(st) == 0:
                flag = 0
            else:
                if doesMatch(st[-1], ch):
                    st.pop()     #at the time of closing bracket shift ch_count to max_count
                    ch_count += 2
                    max_count = max(ch_count, max_count)


    return max_count

def isOpening(ch):
    return ch == "("

def doesMatch(och, cch):
    return och == "(" and cch == ")"

s = "((())(()"
print(longestValidParentheses(s))
s =")()())"
print(longestValidParentheses(s))
s = "()(()"
print(longestValidParentheses(s))

