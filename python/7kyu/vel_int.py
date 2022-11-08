def gps(s, x):
    max_vel = 0
    for i in range(0, len(x)-1):
        v = (x[i+1] - x[i]) / s
        if v > max_vel:
            max_vel = v
    return int(max_vel*3600)