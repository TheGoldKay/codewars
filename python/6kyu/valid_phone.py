def valid_phone_number(p):
    print(p)
    p = p.lower()
    l = p.split(' ')
    le = len(l[0])
    if not l[0][1:-1].isnumeric():
        return False 
    if len(l) >= 2 and len(l[1]) <= 3:
        s = l[1].split('-')
        if len(s) > 1:
            a, b = s
            if len(b) <= 3:
                return False 
    if l[0][0] == '(' and l[0][-1] == ')' and len(l) == 2 and p[le] == ' ' and '-' in l[1] and l[1]:
        if all(map(str.isnumeric, l[1].split('-'))):
            return True
        
    return False