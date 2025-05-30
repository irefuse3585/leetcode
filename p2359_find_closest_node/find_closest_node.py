from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        INF = n + 1

        # 1) Compute distances from node1 to all reachable nodes
        dist1 = [INF] * n
        cur, d = node1, 0
        while cur != -1 and dist1[cur] == INF:
            dist1[cur] = d
            cur = edges[cur]
            d += 1

        # 2) Compute distances from node2 to all reachable nodes
        dist2 = [INF] * n
        cur, d = node2, 0
        while cur != -1 and dist2[cur] == INF:
            dist2[cur] = d
            cur = edges[cur]
            d += 1

        # 3) Find the node with minimal max(dist1[i], dist2[i])
        bestNode = -1
        bestCost = INF
        for i in range(n):
            if dist1[i] == INF or dist2[i] == INF:
                continue
            cost = max(dist1[i], dist2[i])
            if cost < bestCost or (
                cost == bestCost and (bestNode == -1 or i < bestNode)
            ):
                bestCost, bestNode = cost, i

        return bestNode
