def narcissistic(num):
    p = len(str(num))
    s = 0
    for i in map(int, str(num)):
        s += i ** p 
    return s == num 

print(narcissistic(371))
print(narcissistic(122))
