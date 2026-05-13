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


if __name__ == "__main__":
    s = Solution().mergeAlternately
    tests = [
        (("abc", "pqr"), "apbqcr"),
        (("ab", "pqrs"), "apbqrs"),
        (("abcd", "pq"), "apbqcd"),
        (("a", "z"), "az"),
    ]
    for (w1, w2), want in tests:
        got = s(w1, w2)
        assert got == want, (w1, w2, got, want)
    print("All tests passed:", len(tests), "cases")

