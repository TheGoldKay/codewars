def explode(s):
    res = ""
    for n in s:
        res += n * int(n)
    return res