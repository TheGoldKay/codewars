def reverse_words(text):
    ans = []
    for s in text.split(' '):
        ans.append(s[::-1])
    return ' '.join(ans)