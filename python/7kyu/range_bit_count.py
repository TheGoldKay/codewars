def range_bit_count(a, b):
    count = 0
    for num in range(a, b+1):
        b = bin(num)[2:]
        count += b.count('1')
    return count 

print(range_bit_count(2, 7))