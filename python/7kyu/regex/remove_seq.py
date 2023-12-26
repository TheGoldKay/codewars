import re 

def remove_consecutive_duplicates(s : str) -> str:
    l = s.split(' ')
    if(len(l) > 1):
        res = [l[0]]
        for i in range(1, len(l) - 1):
            if(l[i] != l[i-1]):
                res.append(l[i])
        if(l[-1] != l[-2]):
            res.append(l[-1])
        return " ".join(res)   
    else:
        return l[0]

def remove_consecutive_duplicates(s):
    return re.sub(r"\b(\w+)(\s(\1\b))+", r"\1", s)