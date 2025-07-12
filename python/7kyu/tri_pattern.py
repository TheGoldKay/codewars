def pattern(n: int) -> str:
    ans: list = []
    for i in range(n):
        st: str = " " * i + str(i + 1) * (n - i)
        ans.append(st)
    return "\n".join(ans)