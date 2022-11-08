def tribonacci(sig, n):
    if n < 3:
        return sig[:n]
    while len(sig) < n:
        sig.append(sum(sig[-3:]))
    return sig 

print(tribonacci([1,1,1], 10))
