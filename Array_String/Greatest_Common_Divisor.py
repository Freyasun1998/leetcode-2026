"""
Greatest Common Divisor of Strings
LeetCode 1146 - Difficulty: Easy

For two strings 's' and 't', we say "'t' divides 's'" if and only if 's = t + t + t + ... + t + t' (i.e., 't' is concatenated with itself one or more times).

Given two strings 'str1' and 'str2', 
return the largest string 'x' such that 'x' divides both 'str1' and 'str2'.



Constraints:

• '1 <= str1.length, str2.length <= 1000'

• 'str1' and 'str2' consist of English uppercase letters.
"""
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        g = gcd(len(str1), len(str2))
        return str1[:g]


def test_gcd_classic_example() -> None:
    assert Solution().gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_gcd_no_common_divisor() -> None:
    assert Solution().gcdOfStrings("LEET", "CODE") == ""


def test_gcd_identical_strings() -> None:
    assert Solution().gcdOfStrings("ABAB", "ABAB") == "ABAB"


def test_gcd_shorter_divides_longer() -> None:
    assert Solution().gcdOfStrings("ABABAB", "AB") == "AB"


def test_gcd_repeated_single_character() -> None:
    assert Solution().gcdOfStrings("AAAA", "AA") == "AA"


def test_gcd_coprime_repeat_counts() -> None:
    # gcd(6, 4) = 2 → "AB", not the full "ABABAB"
    assert Solution().gcdOfStrings("ABABAB", "ABAB") == "AB"
