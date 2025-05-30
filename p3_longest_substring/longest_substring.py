class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        max_len = left = 0
        for right, ch in enumerate(s):
            if ch in last_pos and last_pos[ch] >= left:
                left = last_pos[ch] + 1
            last_pos[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len
