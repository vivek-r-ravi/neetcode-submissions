"""
There is a new alien language that uses the English alphabet, 
but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. 
It is claimed that the strings in words are sorted lexicographically by 
the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words 
cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language 
sorted in lexicographically increasing order by the new language's rules. 
If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:
* The first letter where they differ is smaller in a than in b.
* a is a prefix of b and a.length < b.length.


Example 1:
Input: words = ["z","o"]
Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".


Example 2:
Input: words = ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"
"""


# BFS (Kahn's algorithm)
# O(N+V+E) time, O(V+E) space
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj_list = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj_list}
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w2[j] != w1[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])
        top_sort = []
        while q:
            curr = q.popleft()
            top_sort.append(curr)
            for nei in adj_list[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(top_sort) if len(adj_list) == len(top_sort) else ""


# DFS Topological Sort
# O(N+V+E) time, O(V+E) space
class SolutionV2:
    def foreignDictionary(self, words: List[str]) -> str:

        adj_list = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w2[j] != w1[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                    break

        state = {c: 0 for w in words for c in w}  # 0 = unvisited, 1 = visiting, 2 = visited
        topSort = []

        def dfs(src: str) -> bool:
            if state[src] == 2:  # already visited
                return True
            if state[src] == 1:  # already visiting
                return False
            state[src] += 1      # visiting
            for neighbor in adj_list[src]:
                if not dfs(neighbor):
                    return False
            state[src] += 1  # visited
            topSort.append(src)
            return True

        for c in state:
            if not dfs(c):
                return ""
        
        topSort.reverse()
        return "".join(topSort)