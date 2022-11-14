def highest_rank(arr):
    m = [0, 0]
    for e in arr:
        if arr.count(e) > m[0]:
            m = [arr.count(e), e]
        if arr.count(e) == m[0]:
            if e > m[1]:
                m[1] = e
    return m[1]