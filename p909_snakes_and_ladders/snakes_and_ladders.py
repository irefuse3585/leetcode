from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n * n

        # Special case: if there's only one square, we're already at the end
        if n2 == 1:
            return 0

        # 1. Build 1D array `dest` of length (n2 + 1):
        #    dest[i] = destination square if you land on i (snake/ladder) or i itself.
        dest = [0] * (n2 + 1)
        idx = 1
        for row in range(n - 1, -1, -1):
            is_left_to_right = (n - 1 - row) % 2 == 0
            if is_left_to_right:
                for col in range(0, n):
                    val = board[row][col]
                    dest[idx] = val if val != -1 else idx
                    idx += 1
            else:
                for col in range(n - 1, -1, -1):
                    val = board[row][col]
                    dest[idx] = val if val != -1 else idx
                    idx += 1

        # 2. Initialize distances array: dist[i] = -1 means "unvisited".
        dist = [-1] * (n2 + 1)
        dist[1] = 0  # Start at square 1 with 0 moves

        # 3. Use a Python list as a queue with head pointer for O(1) pop from front
        queue = [1]
        head = 0

        # 4. Standard BFS loop
        while head < len(queue):
            curr = queue[head]
            head += 1
            moves = dist[curr]

            # Try dice rolls from 1 to 6
            for step in range(1, 7):
                nxt = curr + step
                if nxt > n2:
                    break
                target = dest[nxt]
                if dist[target] == -1:
                    dist[target] = moves + 1
                    if target == n2:
                        return dist[target]
                    queue.append(target)

        # 5. If BFS finished without reaching n2, it's unreachable
        return -1
