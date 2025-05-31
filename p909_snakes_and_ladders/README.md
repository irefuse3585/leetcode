# LeetCode #909: Snakes and Ladders

## 📖 Problem

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a Boustrophedon style starting from the bottom-left of the board (`board[n - 1][0]`) and alternating direction each row.

You start on square `1`. In each move, starting from square `curr`, do the following:

1. Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n^2)]`.  
   - This simulates the result of a standard 6-sided die roll: there are at most 6 possible destinations.
2. If `next` has a snake or ladder (`board[r][c] != -1` for its coordinates `(r, c)`), you **must** move to `board[r][c]`. Otherwise, you stay on `next`.
3. The game ends when you reach square `n^2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n^2` are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination of a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

Return the least number of dice rolls required to reach square `n^2`. If it is not possible to reach that square, return `-1`.

### Example 1

```
Input: 
board = [
  [-1, -1, -1, -1, -1, -1],
  [-1, -1, -1, -1, -1, -1],
  [-1, -1, -1, -1, -1, -1],
  [-1, 35, -1, -1, 13, -1],
  [-1, -1, -1, -1, -1, -1],
  [-1, 15, -1, -1, -1, -1]
]
Output: 4

Explanation:
Boustrophedon labeling (6×6):
Row 0 (top):      36  35  34  33  32  31
Row 1:            25  26  27  28  29  30
Row 2:            24  23  22  21  20  19
Row 3:            13  14  15  16  17  18
Row 4:            12  11  10   9   8   7
Row 5 (bottom):    1   2   3   4   5   6

One optimal sequence:
- Start at 1.
- Roll 1 → move to 2, ladder sends you to 15.
- From 15, roll 2 → move to 17, snake sends you to 13.
- From 13, roll 1 → move to 14, ladder sends you to 35.
- From 35, roll 1 → move to 36 (end).
Total rolls = 4.
```

### Example 2

```
Input:
board = [
  [-1, -1],
  [-1,  3]
]
Output: 1

Explanation:
Boustrophedon labeling (2×2):
Row 1 (bottom):    1   2
Row 0 (top):       4   3
From 1, roll 1 → land on 2, ladder sends you to 3 (end). Total rolls = 1.
```

### Constraints

- `n == board.length == board[i].length`  
- `2 <= n <= 20`  
- `board[i][j]` is either `-1` or in the range `[1, n^2]`.  
- Squares labeled `1` and `n^2` are not the starting points of any snake or ladder.

---

## 🚀 Solution (O(n²))

1. **Handle edge case `n = 1`.**  
   - If `n == 1`, then `n^2 == 1`, start and end are the same square → return `0`.

2. **Flatten the board into a 1D array `dest[]` of length `n^2 + 1`.**  
   - Let `n2 = n * n`.  
   - Create `dest = [0] * (n2 + 1)` and an index `idx = 1`.  
   - Iterate rows from bottom to top:
     ```python
     idx = 1
     for row in range(n - 1, -1, -1):
         left_to_right = ((n - 1 - row) % 2 == 0)
         if left_to_right:
             for col in range(0, n):
                 val = board[row][col]
                 dest[idx] = val if val != -1 else idx
                 idx += 1
         else:
             for col in range(n - 1, -1, -1):
                 val = board[row][col]
                 dest[idx] = val if val != -1 else idx
                 idx += 1
     ```
   - After this `O(n²)` pass, `dest[k]` gives the final landing square if you “land” on `k`, following exactly one snake/ladder if present.

3. **Perform BFS over 1D squares (1 to n²).**  
   - Create an array `dist = [-1] * (n2 + 1)`, set `dist[1] = 0`.  
   - Use a list `queue = [1]` and a head pointer `head = 0` for `O(1)`-time pops:
     ```python
     dist = [-1] * (n2 + 1)
     dist[1] = 0
     queue = [1]
     head = 0

     while head < len(queue):
         curr = queue[head]
         head += 1
         steps = dist[curr]

         for move in range(1, 7):             # simulate die = 1..6
             nxt = curr + move
             if nxt > n2:
                 break                       # beyond n², no valid moves
             target = dest[nxt]             # apply one snake/ladder
             if dist[target] == -1:         # not visited yet
                 dist[target] = steps + 1
                 if target == n2:
                     return dist[target]     # reached end in minimal rolls
                 queue.append(target)

     return -1  # if BFS finishes without reaching n², return -1
     ```
   - **Why BFS?** Each dice roll counts as one move of weight=1. BFS finds the minimum number of moves to reach `n^2`.

4. **Return result.**  
   - If BFS reaches `n2`, return the corresponding `dist[n2]`.  
   - Otherwise, return `-1`.

---

## 🔢 Example Walkthrough

```
board = [
  [-1, -1, -1],
  [-1,  9,  8],
  [-1,  6, -1]
]
# n = 3, n2 = 9
# Boustrophedon labeling (3×3):
#    1    2    3
#    6    5    4
#    7    8    9
# dest mapping:
#   dest[1] = 1
#   dest[2] = 9   (ladder)
#   dest[3] = 3
#   dest[4] = 4
#   dest[5] = 5
#   dest[6] = 6
#   dest[7] = 7
#   dest[8] = 8
#   dest[9] = 9
#
# BFS:
#   dist[1] = 0
#   queue = [1]
#   head = 0
#
#   Dequeue curr = 1 (steps = 0):
#     moves: 1+1=2 -> dest[2] = 9 -> dist[9] = 1 -> return 1
#   Output: 1
```

## 📊 Complexity

- **Time:**  
  - Building `dest[]` is `O(n²)`.  
  - BFS visits each square at most once and checks up to 6 neighbors → `O(6 · n²) = O(n²)`.  
  - Overall: **O(n²)**.

- **Space:**  
  - `dest[]` of size `n² + 1`.  
  - `dist[]` of size `n² + 1`.  
  - `queue` holds up to `n²` indices in the worst case.  
  - Overall: **O(n²)**.
