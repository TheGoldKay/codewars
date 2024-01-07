import re

def make_string(s):
    return "".join(c[0] for c in s.split(" "))

def make_string2(s):
    return re.sub(r'\b\w', '', s)
