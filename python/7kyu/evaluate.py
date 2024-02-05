
calc = lambda a, b: (a + b) + (a - b) + (a * b) + (a // b) if b != 0 else None

def evaluate(eq):
    seq = [int(n) for n in eq.replace(" ", "").split("@")]
    if len(seq) < 2:
        return seq[0]
    res = calc(seq[0], seq[1])
    if res == None:
        return None
    seq = seq[2:]
    while seq:
        res = calc(res, seq[0])    
        if res == None:
            return None
        del seq[0]
    return res