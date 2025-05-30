import pytest

from p3_longest_substring.longest_substring import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # "abc" of length 3
        ("bbbbb", 1),  # "b" of length 1
        ("pwwkew", 3),  # "wke" of length 3
        ("", 0),  # empty string
        (" ", 1),  # single space
        ("au", 2),  # "au" of length 2
        ("dvdf", 3),  # "vdf" of length 3
    ],
)
def test_length_of_longest_substring(s: str, expected: int):
    assert Solution().lengthOfLongestSubstring(s) == expected
