def smallest_transform(num):
    s = [int(s) for s in str(num)]
    least = float('inf')
    for n in s:
        steps = sum(map(lambda x: abs(n - x), s))
        if steps < least:
            least = steps
    return least


print(smallest_transform(399)) 