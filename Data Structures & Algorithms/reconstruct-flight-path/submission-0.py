# brute force: DFS Backtracking
# O(EV) time space
class SolutionV1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res


# Eulerian Path Problem: use every edge once
# Heirholzer DFS: append node (post order) after consuming all outgoing edges
# lexicographically smallest ensured by sorted adj list in reverse order
# O(ElogE) time O(E) space
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        out = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            out.append(src)

        dfs("JFK")
        return out[::-1]
