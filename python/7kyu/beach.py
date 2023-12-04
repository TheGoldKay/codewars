import re

def counter(arr, s):
    """
    Counts the number of times a substring appears in a given list.

    Parameters:
        arr (list): The list to search for the substring.
        s (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the list.
    """
    l = len(s)
    i = 0 
    ct = 0
    while i < len(arr):
        if arr[i: i+l] == s:
            ct += 1
            i += l  
        else:
            i += 1
    return ct 

def sum_of_a_beach(beach):
    words = ["sun", "sand", "water", "fish"]
    count = 0
    b = beach.lower()
    for w in words:
        count += beach.count(w)
    return count

def sum_of_a_beach2(beach):
    words = ["sun", "sand", "water", "fish"]
    beach_lower = beach.lower()

    # Create a regular expression pattern by joining the words with the "|" (OR) operator
    pattern = "|".join(words)

    # Use re.findall to find all occurrences of the pattern in the lowercased beach string
    matches = re.findall(pattern, beach_lower)

    # Return the count of matches
    return len(matches)

print(counter("sunsunsunsun", "sun"))