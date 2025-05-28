# LeetCode #3: Longest Substring Without Repeating Characters

## 📖 Problem

Given a string `s`, find the length of the longest substring without repeating characters.  
- **Input:** a string `s` (may be empty, can contain any characters).  
- **Output:** an integer — the length of the longest substring without duplicate characters.

## 🚀 Solution (O(n))

1. Initialize:  
   - `last_pos = {}` — a dictionary to store the last index of each character.  
   - `left = 0` — the left boundary of the sliding window.  
   - `max_len = 0` — the maximum length found so far.

2. Iterate through the string in one pass:  
   ```python
   for right, ch in enumerate(s):
       if ch in last_pos and last_pos[ch] >= left:
           # if the character repeats within current window,
           # move the left boundary right after its previous occurrence
           left = last_pos[ch] + 1
       # update the last occurrence of the character
       last_pos[ch] = right
       # update the maximum length
       max_len = max(max_len, right - left + 1)
   ```

3. Return `max_len`.

## 🔢 Example

```
s = "pwwkew"
# result → 3  # substring "wke"
```

## 📊 Complexity

- **Time:** O(n) — each character is processed once, dictionary lookups are O(1).  
- **Space:** O(min(n, Σ)) — we store last positions for characters (Σ = size of the character set).
