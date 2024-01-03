def count_developers(lst: list) -> int:
    return sum(map(lambda dev: dev['continent'] == 'Europe' and dev['language'] == 'JavaScript', lst))