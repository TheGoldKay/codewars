def smallest_transform(num):
    s = list(str(num))
    least = float('inf')
    for n in s:
        steps = sum(map(lambda x: abs(int(n) - int(x)), s))
        if steps < least:
            least = steps
    return least


print(smallest_transform(399)) 