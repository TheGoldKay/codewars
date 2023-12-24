def nonstop_hotspot(area):
    left = area.index('P') - 1
    right = left + 2
    hs = 0
    while (left >= 0):
        if(area[left] == '#'):
            break 
        else:
            if(area[left] == '*'):
                hs += 1
            left -= 1
    while(right < len(area)):
        if(area[right] == '#'):
            break 
        else:
            if(area[right] == '*'):
                hs += 1
            right += 1
    return hs 

def nonstop_hotspot(area):
    for part in area.split('#'):
        if 'P' in part:
            return part.count('*')
    

s1 = '*   P  *   *'
s2 = '*  * #  * P # * #'
print(nonstop_hotspot(s2))