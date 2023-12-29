import re

def remove_chars(s):
    #return re.sub(r'[^a-zA-Z ]', '', s) # just place a natural ' ' space right there
    return " ".join(map(lambda st: re.sub(r'[^a-zA-Z]', '', st), s.split(" "))) 