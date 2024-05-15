def bitapp(text, pattern):
    m = len(pattern)

    if m == 0:
        return text
    R = [0]*(m+1)
    R[0]=1

    for i in range(len(text)):
        for k in range(m, 0, -1):
            R[k] = (R[k - 1] & (text[i] == pattern[k - 1]))


            if R[m]:
                return  text[i - m + 1:i + 1]
    return None

print(bitapp("hellojithiaweutbn","hell"))

