# Trie DFS 
# O(w) time for addWord and search, O(t) space
# w is word length, t is number of nodes in the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:

        def dfs(node, idx):
            if idx == len(word):
                return node.word

            c = word[idx]
            
            if c != "." and c not in node.children:
                return False

            if c != ".":
                return dfs(node.children[c], idx + 1)
            else:
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False

        return dfs(self.root, 0)
