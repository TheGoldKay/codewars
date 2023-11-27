def stray(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n 

def stray2(arr):
    for i in range(1, len(arr), 2):
        if arr[i] == arr[i-1] and arr[i] != arr[i+1]:
            return arr[i+1]
        elif arr[i] == arr[i+1] and arr[i] != arr[i-1]:
            return arr[i-1]
        elif  arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            return arr[i]