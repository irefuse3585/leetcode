# LeetCode #2: Add Two Numbers

## 📖 Problem

You are given two non-empty singly linked lists (`ListNode`) representing two non-negative integers.  
Digits are stored in reverse order (least significant digit at the head).  
Each node contains a single digit (0–9).  

Add the two numbers and return the sum as a linked list in the same reverse order.

## 🚀 Solution (O(n))

1. Initialize:  
   - `dummy = ListNode(0)` — dummy head of the result list.  
   - `tail = dummy` — pointer to the tail of the result.  
   - `carry = 0` — carry for the next digit.

2. While there are nodes in `l1` or `l2`, or `carry` is non-zero:  
   ```python
   v1 = l1.val if l1 else 0
   v2 = l2.val if l2 else 0
   carry, digit = divmod(v1 + v2 + carry, 10)
   tail.next = ListNode(digit)
   tail = tail.next
   l1 = l1.next if l1 else None
   l2 = l2.next if l2 else None
   ```

3. Return `dummy.next` as the head of the summed list.

## 🔢 Example

```
l1 = [2,4,3]   # 342
l2 = [5,6,4]   # 465
result → [7,0,8]  # 807
```

## 📊 Complexity

- Time: O(max(n, m))  
- Space: O(max(n, m))
