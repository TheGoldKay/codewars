def rank(lst):
    d = {}
    for rk, val in enumerate(sorted(lst)):
        if not d.get(val):
            d[val] = [rk]
        else:
            d[val].append(rk)
    return [sum(d[arg]) / len(d[arg]) for arg in lst]

print(rank([1, 3, 3, 9, 8]))            