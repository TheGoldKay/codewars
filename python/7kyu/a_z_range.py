from string import ascii_lowercase as alpha

def gimme_the_letters(sp):
    if sp[0].islower():
        return alpha[alpha.index(sp[0]): alpha.index(sp[-1]) + 1]
    else:
        a = alpha.upper()
        return a[a.index(sp[0]): a.index(sp[-1]) + 1]