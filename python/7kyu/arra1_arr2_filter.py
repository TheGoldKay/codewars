def find_array(arr1, arr2):
    return list(map(lambda i: arr1[i], filter(lambda n: n < len(arr1), arr2)))