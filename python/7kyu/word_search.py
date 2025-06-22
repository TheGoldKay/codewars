import re

f = re.I

def word_search(query: str, seq: list[str]) -> list[str]:
    query_lower: str = query.lower()
    filtered: list[str] = list(filter(lambda word: query_lower in word.lower(), seq))
    return filtered if len(filtered) else ['None']

word_search("ab", ["za", "ab", "abc", "zab", "zbc"])