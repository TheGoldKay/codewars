def vowel_2_index(string):
    news = ""
    for i, s in enumerate(string, 1):
        if s in "aeiouAEIOU":
            news += str(i)
        else:
            news += s
    return news