def possibly_perfect(key, answers):
    correct = True
    wrong = True
    for i in range(len(key)):
        if key[i] != '_':
            correct = correct and key[i] == answers[i]
            wrong = wrong and key[i] != answers[i]
    return correct or wrong