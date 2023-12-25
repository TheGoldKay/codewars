import re 

def purify(s: str) -> str:
    res = []
    for house in s.split(' '):
        # add a space so the next line doesn't erase any neighboring 'i'
        h = re.sub(r'ii', 'isi', house, flags=re.IGNORECASE)
        # sub whatever to the left and right of 'i' for ''
        newh = re.sub(r'.?i.?', '', h, flags=re.IGNORECASE)
        if newh:
            res.append(newh)
    return " ".join(res)

def purify2(s: str) -> str:
    s = s.replace('I', 'i')
    s = list(s)
    indexes = []
    for i in range(len(s)):
        if s[i] == 'i' and i != 0 and i != len(s) - 1:
            if s[i-1] != ' ':
                indexes.append(i-1)
            indexes.append(i)
            if s[i+1] != ' ':
                indexes.append(i+1)
        elif s[i] == "i" and i == 0:
            indexes.append(0)
            indexes.append(1)
        elif s[i] == 'i' and i == len(s) - 1:
            indexes.append(len(s)-1)
            indexes.append(len(s)-2)
    indexes = list(set(indexes))
    indexes = sorted(indexes, reverse=True)

    for i in indexes:
        del s[i]
    s = ''.join(s)
    s = s.strip()
    for i in range(10):
        s = s.replace('  ', ' ')
    return s

print(purify("STRING"))
        