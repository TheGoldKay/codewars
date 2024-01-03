def add_binary(a,b):
    n = a + b
    binList = []
    while (n > 0):
        binList.append(n % 2)
        n = n // 2
    return ''.join(map(str, reversed(binList)))

def add_binary2(a, b):
    return bin(a+b)[2:]

print(add_binary(2, 2))
  