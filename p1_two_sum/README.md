# LeetCode #1: Two Sum

**Problem:**  
Given an array `nums` and a number `target`, find indices of the two numbers such that they add up to `target`.

**Solution Idea:**  
Use a hash map in one pass O(n):  
1. For each `num`, compute `need = target - num`.  
2. If `need` has already been seen — return the pair of indices.  
3. Otherwise, store `num → its index` in the map.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

**Example:**
```python
nums = [2,7,11,15]
target = 9
# → [0,1]
```
