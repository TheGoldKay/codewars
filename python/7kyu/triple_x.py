def triple_x(s):
    if 'x' in s:
        i = s.index('x')
        return s[i+1: i+3] == 'xx'
    else:
        return False 