from itertools import cycle 

def increment(number, iterations, spacer):
    num = str(number)
    lst = list(map(int, num))
    seq = cycle(range(len(num)))
    current = next(seq)
    index = 1
    for i in range(iterations):
        print("---")
        for _ in range(spacer):
            current = next(seq)
            index += 1
            if (index >= len(lst)):
                index = 0
                current = next(seq)
            print(current)
        print("-")
        lst[current] += 1
        print(lst[current], i)
        print(lst)
        print("****")
        lst = list(map(int, "".join(map(str, lst))))
    return int("".join(map(str, lst)))

print(increment(9999,9,9), 32211)
                                