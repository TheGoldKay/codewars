from collections import OrderedDict

def ordered_count(inp) -> list[tuple]:
    counter: OrderedDict[str, int] = OrderedDict()
    for c in inp:
        if counter.get(c):
            counter[c] += 1
        else:
            counter[c] = 1
    return [(c, num) for c, num in counter.items()]