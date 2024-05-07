def tail(s):
    return s[:-1]

def head(s):
    return s[-1]

def ldistance(s,t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    if head(s) == head(t) :
        cost = 0
    else:
        cost = 1


    distance = min(ldistance(tail(s),t)+1,ldistance(s,tail(t))+1,ldistance(tail(s),tail(t))+cost)
    return distance

print(ldistance('hello','seldom'))
print(ldistance('irks','risk'))
