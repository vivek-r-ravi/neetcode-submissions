"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# DFS + hashmap
# O(V+E) time O(V) space
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        old_new_map = {}

        def dfs(node):
            if not node:
                return None
            if node in old_new_map:
                return old_new_map[node]
            vertex = Node(node.val)
            old_new_map[node] = vertex
            for neighbor in node.neighbors:
                vertex.neighbors.append(dfs(neighbor))
            return vertex

        return dfs(node)


# BFS + hashmap
# O(V+E) time O(V) space
class SolutionV2:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        old_new_map = {}
        old_new_map[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old_new_map:
                    old_new_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old_new_map[cur].neighbors.append(old_new_map[neighbor])

        return old_new_map[node]