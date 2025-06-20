from typing import Union

class Test:
    def assert_equals(self, passed: Union[str, int], expected: Union[str, int], _error: str = "") -> None:
        if passed != expected:
            if _error:        
                raise Exception(_error)
            else:
                raise Exception(f"{passed} should be {expected}")