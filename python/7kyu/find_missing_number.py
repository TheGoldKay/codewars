def find_missing_number(sequence: str) -> int:
    if not sequence:
        return 0
    lst: list[int] = []
    for c in sequence.split(" "):
        if not c.isnumeric():
            return 1
        else:
            lst.append(int(c))
    lst.sort()
    for i, num in enumerate(lst, 1):
        if num != i:
            return i
    return 0
        