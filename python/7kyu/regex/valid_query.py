from preloaded import FILTERS
import re

def is_valid(query: str) -> bool:
    return all([tag in FILTERS for tag in re.findall(r'(\w+):', query)])