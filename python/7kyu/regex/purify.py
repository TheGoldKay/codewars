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

print(purify("STRING"))
        