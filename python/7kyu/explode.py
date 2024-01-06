def explode(s):
    res = []
    for n in s:
        res = res + [n] * int(n)
    return "".join(res)