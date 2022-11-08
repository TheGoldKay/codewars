def find_uniq(arr):
    s = list(set(arr))
    if arr.count(s[0]) == 1:
        return s[0]
    else:
        return s[1]