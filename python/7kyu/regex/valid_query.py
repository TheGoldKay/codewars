#from preloaded import FILTERS
import re

FILTERS = "" # this is provided by codewars.com api
def is_valid(query: str) -> bool:
    return all([tag in FILTERS for tag in re.findall(r'(\w+):', query)])