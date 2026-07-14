# BFS + word pattern hash map
# O(nm^2) time, O(nm) space
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList + [beginWord]:
            for j in range(n):
                pattern = word[:j] + "*" + word[j + 1 :]
                adj[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        out = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return out
                for j in range(n):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for w in adj[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)
            out += 1
        return 0
