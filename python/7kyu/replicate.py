
def replicate(times, number):
    if times <= 0:
        return []
    return replicate(times - 1, number) + [number]

print(replicate(3, 5))