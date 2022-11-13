def triple_double(num1, num2):
    n1 = str(num1)
    n2 = str(num2)
    a = dict()
    b = dict()
    t, d = False, False 
    num = 0
    for i in range(len(n1)-1):
        if n1[i] == n1[i+1] and n1[i+1] == n1[i+2]:
            t = True 
            num = n1[i]
            break
    for i in range(len(n2)-1):
        if n2[i] == n2[i+1] and n2[i] == num:
            d = True 
            break
        
    return 1 if t and d else 0
        