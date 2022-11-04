def vowel_one(s):
    
    v = "aAeEiIoOuU"
    news = ''
    for c in s:
        if c in v:
            news += '1'
        else:
            news += '0'
    return news