def good_vs_evil(good, evil):
    g = [1, 2, 3, 3, 4, 10]
    s1 = 0
    e = [1, 2, 2, 2, 3, 5, 10]
    s2 = 0
    for i, j in zip(g, map(int, good.split(' '))):
        s1 += j * i
    for i, j in zip(e, map(int, evil.split(' '))):
        s2 += j * i
    if s1 > s2:
        ans = 'Good triumphs over Evil'
    elif s1 < s2:
        ans = 'Evil eradicates all trace of Good'
    else:
        ans = 'No victor on this battle field'
    return f"Battle Result: {ans}"