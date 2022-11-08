def delete_nth(order,max_e):
    a = []
    for e in order:
        if a.count(e) <  max_e:
            a.append(e)
    return a