def win(a, b, c):
    #a, b, c = sorted([a, b, c])
    if (b - a) == (c - b):
        return True
    elif (c - a) == (b - c):
        return True

def block_player(a, b):
    for c in range(9):
        if win(a, b, c):
            return c

def block_player2(a, b):
    wins = (
    #   horizontal    vertical      diagonal
        (0, 1, 2),    (0, 3, 6),    (0, 4, 8),
        (3, 4, 5),    (1, 4, 7),    (2, 4, 6),
        (6, 7, 8),    (2, 5, 8)
    )
    for win in wins:
        if a in win and b in win:
            return sum(win) - a - b

def block_player3(a, b):
    y1, x1 = divmod(a, 3) 
    y2, x2 = divmod(b, 3)
    y3 = (y2 + (y2 - y1)) % 3
    x3 = (x2 + (x2 - x1)) % 3
    return y3 * 3 + x3