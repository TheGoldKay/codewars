def high(x):
    m = [0, '']
    for w in x.split(' '):
        s = list(map(lambda i: ord(i) - 96 if i.isalpha() else 0, w))
        s = sum(s)
        if s > m[0]:
            m = [s, w]
    return m[1]