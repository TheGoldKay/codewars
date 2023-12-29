import re 

def remove_bmw(string):
    if type(string) != str:
        raise TypeError("This program only works for text.")
    return re.sub(r"[bmwBMW]", "", string)