def camel_case(string):
    return "".join(map(str.capitalize, string.split(" ")))