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
