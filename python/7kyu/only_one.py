from typing import Callable

def one(xs: list[int], f: Callable[[int], bool]) -> bool: 
    one_max: int = 0
    for num in xs:
        one_max += f(num)
        if one_max > 1:
            return False
    return True

def shorter(xs: list[int], f: Callable[[int], bool]) -> bool:
    return sum(map(f, xs)) == 1