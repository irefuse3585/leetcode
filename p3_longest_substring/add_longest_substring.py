class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            max_len = 1
            current = s[0]
            for i in range(1, len(s)):
                if s[i] not in current:
                    current += s[i]
                    if len(current) > max_len:
                        max_len = len(current)
                else:
                    if s[i] == s[i-1]:
                        current = s[i]
                    else:
                        idx = current.find(s[i])
                        current = current[idx+1:] + s[i]
            return max_len