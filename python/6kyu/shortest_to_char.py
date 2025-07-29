def shortest_to_char(s: str, c: str) -> list[int]:
    if (s == '' or c == '' or c not in s):
        return []
    res: list[int] = []
    ln: int = len(s)
    for i in range(ln):
        left: str = s[:i+1][::-1]
        right: str = s[i:]
        closest: int = ln
        if (c in left):
            closest = left.index(c)
        if (c in right):
            r = right.index(c) - i + (ln - len(right))
            if (r < closest):
                closest = r
        res.append(closest)
    return res