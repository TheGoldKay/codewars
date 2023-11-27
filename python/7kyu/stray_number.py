def stray(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n 