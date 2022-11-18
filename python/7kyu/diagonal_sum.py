def diagonal_sum(array):
    index = 0
    s = 0
    while index < len(array):
        s += array[index][index]
        index += 1
    return s 


array = [[5, 9, 1, 0],
         [8, 7, 2, 3],
         [1, 4, 1, 9],
         [2, 3, 8, 2]]

print(diagonal_sum(array))