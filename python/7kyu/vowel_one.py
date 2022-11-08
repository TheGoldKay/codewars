def vowel_one(s):
    
    v = "aAeEiIoOuU"
    news = ''
    for c in s:
        if c in v:
            news += '1'
        else:
            news += '0'
    return news

def vowel_one(s):
    return "".join(map(lambda x: '1' if x in "aAeEiIoOuU" else '0', s))   