from test import Test

def check_vowel(strng: str, position: int) -> bool:
    return strng[position] in "aeiouAEIOU" if position < len(strng) and position >= 0 else False


def basic_test_cases() -> None:
    test: Test = Test()
    test.assert_equals(check_vowel('cat', 1), True, "Should equal 'true'")
    test.assert_equals(check_vowel('cat', 0), False, "Should equal 'false'")
    test.assert_equals(check_vowel('cat', 4), False, "Should equal 'false'")  
    test.assert_equals(check_vowel('Amanda', -2), False, "Should equal 'false'")
    test.assert_equals(check_vowel('Amanda', 0), True, "Should equal 'true'")
    test.assert_equals(check_vowel('Amanda', 2), True, "Should equal 'true'")
    
basic_test_cases()