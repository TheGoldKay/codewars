def parse(data):
    out = []
    i = 0
    for c in data:
        if c == 'i':
            i += 1
        elif c == 'd':
            i -= 1
        elif c == 's':
            i = i*i
        elif c == 'o':
            out.append(i)
    return out