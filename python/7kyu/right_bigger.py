def solve(arr) -> list:
    ln: int = len(arr)
    bigger: list = []
    for i, num in enumerate(arr):
        is_bigger: bool = True
        index: int = i + 1
        while index < ln:
            if arr[index] >= num:
                is_bigger = False
                break
            index += 1
        if is_bigger:
            bigger.append(num)
    return bigger