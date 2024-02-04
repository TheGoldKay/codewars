def set_reducer(arr):
    ln = len(arr)
    if ln == 1:
        return arr[0]
    narr = []
    i = 0
    while i < ln:
        if i + 1 < ln and arr[i] == arr[i + 1]:
            count = 1
            while i + 1 < ln and arr[i] == arr[i + 1]:
                i += 1
                count += 1
            narr.append(count)
        else:
            if i == 0 or i == ln - 1:
                narr.append(1)
            elif arr[i - 1] != arr[i] and arr[i] != arr[i + 1]:
                    narr.append(1)
            else:
                narr.append(arr[i])
        i += 1
    return set_reducer(narr)

arr = [0, 4, 6, 8, 8, 8, 5, 5, 7]
arr2 = [8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]
arr3 = [0, 0, 8, 6, 6, 7, 8, 6, 6, 4, 7, 6, 4, 0, 1, 1, 2, 1, 2, 9, 9, 0, 3, 3, 0, 4]
arr4 = [2, 4, 4, 6, 2, 1, 1, 5, 6, 7, 8, 8, 8, 8, 9, 0, 1, 1, 5, 4, 4]

print(set_reducer(arr4))