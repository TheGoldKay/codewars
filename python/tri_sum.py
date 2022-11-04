def get_sum(n):
    sol = 0
    col = 0
    for row in range(n+1):
        for c in range(col, n+1):
            sol += 2 * row + c + 1
        col += 1
    return sol

get_sum(2)