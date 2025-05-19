# p3_longest_substring/test_longest_substring.py

import pytest
from p3_longest_substring.longest_substring import Solution

@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),   # “abc” длины 3
        ("bbbbb", 1),      # “b” длины 1
        ("pwwkew", 3),     # “wke” длины 3
        ("", 0),           # пустая строка
        (" ", 1),          # один пробел
        ("au", 2),         # “au” длины 2
        ("dvdf", 3),       # “vdf” длины 3
    ]
)
def test_length_of_longest_substring(s: str, expected: int):
    assert Solution().lengthOfLongestSubstring(s) == expected
