from dataclasses import dataclass, field

@dataclass
class Check:
    len: int = 6
    invalid: str = "05789"
    span: list[int] = field(default_factory=lambda: [ord('0'), ord('9')])

def zipvalidate(postcode: str) -> bool:
    check: Check = Check()
    if len(postcode) != check.len or postcode[0] in check.invalid:
        return False
    for c in postcode:
        if not (check.span[0] <= ord(c) <= check.span[1]):
            return False
    return True
    