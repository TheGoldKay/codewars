import re, math 

def contact(hallway):
    lst = re.findall(r'(?<=>)-*(?=<)', hallway)
    if len(lst) == 0:
        return -1
    ln = len(min(lst))
    return math.ceil(ln / 2) + (ln % 2 == 0)

hallway = '>---------------<--------------------------<-------->---------<------->----------<----<---->>----------<------->>>---------------<<------>'
hallway2 = '>>-----<<'
hallway3 = '----<----->----'
contact('><')