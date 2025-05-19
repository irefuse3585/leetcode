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
                        idx = s.find(s[i])
                        current = s[:idx]
            return max_len

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))   # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))      # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))     # 3
    print(Solution().lengthOfLongestSubstring(" "))          # 1
    print(Solution().lengthOfLongestSubstring(""))           # 0
