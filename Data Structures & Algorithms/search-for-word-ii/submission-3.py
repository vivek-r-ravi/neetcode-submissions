# brute force: check every word in board
# O(mnk*4^(L)) time where k is numbers of words and L is max length of a word in words
# O(L) space
class SolutionV1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        out = []
        for word in words:
            if self.exist(word):
                out.append(word)
        return out

    def exist(self, word: str) -> bool:

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= self.rows
                or c >= self.cols
                or self.board[r][c] != word[i]
                or self.board[r][c] == "#"
            ):
                return False

            self.board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            self.board[r][c] = word[i]

            return found

        for r in range(self.rows):
            for c in range(self.cols):
                if dfs(r, c, 0):
                    return True

        return False


# trie for pruning
# O(mn*4^(L) + s) time where s is total length of all words in words and L is max length of a word
# O(s) space
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        self.collected = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        out = []
        word_trie = PrefixTree()
        for word in words:
            word_trie.insert(word)

        def dfs(r, c, trie_node):
            if (
                min(r, c) < 0
                or r >= rows
                or c >= cols
                or board[r][c] == "#"
                or board[r][c] not in trie_node.children
            ):
                return

            trie_node = trie_node.children[board[r][c]]
            if trie_node.is_word and not trie_node.collected:
                out.append(trie_node.word)
                trie_node.collected = True

            temp = board[r][c]
            board[r][c] = "#"
            dfs(r + 1, c, trie_node)
            dfs(r - 1, c, trie_node)
            dfs(r, c - 1, trie_node)
            dfs(r, c + 1, trie_node)
            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, word_trie.root)
        
        return out
