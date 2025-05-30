# LeetCode #2359: Find Closest Node to Given Two Nodes

## 📖 Problem

You are given a directed graph of `n` nodes numbered from `0` to `n - 1`, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

Return the index of the node that can be reached from both `node1` and `node2`, such that the maximum between the distance from `node1` to that node and from `node2` to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return `-1`.

Note that `edges` may contain cycles.

### Example 1

```
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation:
The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
```

### Example 2

```
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation:
The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
```

### Constraints

- `n == edges.length`  
- `2 <= n <= 10^5`  
- `-1 <= edges[i] < n`  
- `edges[i] != i`  
- `0 <= node1, node2 < n`

## 🚀 Solution (O(n))

1. **Compute distances**  
   - `dist1 = [INF] * n` — distances from `node1`  
   - `dist2 = [INF] * n` — distances from `node2`  
   - Traverse edges from each start until `-1` or revisiting, filling distances.

2. **Select best node**  
   ```python
   bestNode, bestCost = -1, INF
   for i in range(n):
       if dist1[i] == INF or dist2[i] == INF:
           continue
       cost = max(dist1[i], dist2[i])
       if cost < bestCost or (cost == bestCost and i < bestNode):
           bestCost, bestNode = cost, i
   return bestNode
   ```

## 🔢 Example

```
edges = [5,4,5,4,3,6,-1]
node1 = 0
node2 = 1
# output -> -1  (no common reachable node)
```

## 📊 Complexity

- **Time:** O(n) — each node visited at most twice  
- **Space:** O(n) — two arrays of size n
