def sort_it(lst):
    return sorted(lst, key=lambda item: item if type(item) == int else item[0])