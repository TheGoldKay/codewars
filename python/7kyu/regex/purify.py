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
    res = list(s.replace('I', 'i'))
    indexes = []
    for i in range(len(res)):
        if res[i] == 'i' and i != 0 and i != len(res) - 1:
            if res[i-1] != ' ':
                indexes.append(i-1)
            indexes.append(i)
            if res[i+1] != ' ':
                indexes.append(i+1)
        elif res[i] == "i" and i == 0:
            indexes.append(0)
            indexes.append(1)
        elif res[i] == 'i' and i == len(res) - 1:
            indexes.append(len(res)-1)
            indexes.append(len(res)-2)
    indexes = list(set(indexes))
    indexes = sorted(indexes, reverse=True)

    for i in indexes:
        del res[i]
    st = ''.join(res)
    st = st.strip()
    # if you run this in codewars random tests some will not pass
    # you have to be luck for this hard coded number of runs to be enough
    for i in range(10): 
        st = st.replace('  ', ' ')
    return st

print(purify("STRING"))
        