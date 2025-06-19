from functools import reduce 

left: dict[str, int] = {
    "w": 4,
    "p": 3,
    "b": 2,
    "s": 1, 
}

right: dict[str, int] = {
    "m": 4,
    "q": 3,
    "d": 2,
    "z": 1, 
}

def alphabet_war(fight: str) -> str:
    winner: list[str] = ["Left side wins!", "Right side wins!", "Let's fight again!"]
    p: tuple[int, int] = reduce(
        lambda acc, f: (
            acc[0] + left.get(f, 0),
            acc[1] + right.get(f, 0)
        ),
        fight, 
        (0, 0)
    )
    return winner[2] if p[0] == p[1] else winner[p[1] > p[0]]


def basic_test_cases() -> None:
    assert(alphabet_war("z") == "Right side wins!")
    assert(alphabet_war("zdqmwpbs") == "Let's fight again!")
    assert(alphabet_war("wq") == "Left side wins!")
    assert(alphabet_war("zzzzs") == "Right side wins!")
    assert(alphabet_war("wwwwww") == "Left side wins!")
    print("\t\tAll Green!!!")

basic_test_cases()