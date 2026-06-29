"""
Merge Strings Alternately
LeetCode 1894 - Difficulty: Easy

You are given two strings 'word1' and 'word2'. Merge the strings by adding letters in alternating order, starting with 'word1'. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:

• '1 <= word1.length, word2.length <= 100'

• 'word1' and 'word2' consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        if i < len(word1):
            result.append(word1[i:])
        if i < len(word2):
            result.append(word2[i:])
        return "".join(result)


def test_merge_alternately_equal_length() -> None:
    assert Solution().mergeAlternately("abc", "pqr") == "apbqcr"


def test_merge_alternately_word2_longer() -> None:
    assert Solution().mergeAlternately("ab", "pqrs") == "apbqrs"


def test_merge_alternately_word1_longer() -> None:
    assert Solution().mergeAlternately("abcd", "pq") == "apbqcd"


def test_merge_alternately_single_characters() -> None:
    assert Solution().mergeAlternately("a", "z") == "az"
