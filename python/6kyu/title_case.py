def title_case(title, minor_words=''):
    print(title, ' - ', minor_words)
    s = title.lower()
    if not minor_words:
        return s.title()
    s = s.split(' ')
    s[0] = s[0].title()
    m = minor_words.lower()
    m = m.split(" ")
    for i in range(1, len(s)):
        if not s[i] in m:
            s[i] = s[i].title()
    return " ".join(s)
    