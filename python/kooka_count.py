def kooka_counter(laughing):
    l = laughing.replace('a', '')
    c = 0
    while l:
        print(l)
        if len(l) == 1:
            return c
        if len(l) >= 2 and l[0] == l[1]:
            c += 1
            for i, e in enumerate(l):
                if len(l) >= 2 and l[0] == l[1]:
                    l = l[1:]
        else:
            l = l[1:]
    return c