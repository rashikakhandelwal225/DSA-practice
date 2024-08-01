
def minAddToMakeValid(s):
    st = []
    move = 0
    for ch in s:
        if isOpening(ch):
            st.append(ch)
        else:
            if len(st) == 0:
                if ch == ")":
                    s += "("
                    move += 1
                elif ch == "(":
                    s += ")"
                    move += 1
            else:
                if doesMatch(st[-1], ch):
                    st.pop()

    if len(st) > 0:
        s += ")" * len(st)
        move += len(st)
    return move

def isOpening( ch):
    return ch == "("

def doesMatch(och, cch):
    return och == "(" and cch == ")"

s = '()'
print(minAddToMakeValid(s))
s = '())'
print(minAddToMakeValid(s))
s = '((('
print(minAddToMakeValid(s))