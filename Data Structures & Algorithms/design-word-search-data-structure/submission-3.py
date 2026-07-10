class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if idx == len(word):
                return node.word
            
            if word[idx] != "." and word[idx] not in node.children:
                return False
            
            if word[idx] != ".":
                return dfs(node.children[word[idx]], idx + 1)
            else:
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True

            return False
                    
        return dfs(self.root, 0)
