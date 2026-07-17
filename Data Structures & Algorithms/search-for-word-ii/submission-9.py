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


# trie node carrying DFS + backtracking
# O(mn*4^(L) + S) time where S is total length of all words in words and L is max length of a word
# O(S + L) space
class TrieNodeV2:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""  # add the word at the end for easy retrieval


class PrefixTreeV2:
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


class SolutionV2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        # insert all words into the trie
        out = []
        word_trie = PrefixTree()
        for word in words:
            word_trie.insert(word)

        # DFS on grid while carrying down the tree node
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
            if trie_node.is_word:
                out.append(trie_node.word)
                trie_node.is_word = False  # word added once need not be added again

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


# trie node carrying DFS + backtracking + aggressive pruning
# O(mn*4^(L) + S) time where S is total length of all words in words and L is max length of a word
# O(S + L) space
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_idx = -1  # add the word idx at the end for easy retrieval


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word_idx = idx


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        # insert all words into the trie
        out = []
        word_trie = PrefixTree()
        for i, word in enumerate(words):
            word_trie.insert(word, i)

        # DFS on grid while carrying down the tree node
        def dfs(r, c, trie_node):
            if (
                min(r, c) < 0
                or r >= rows
                or c >= cols
                or board[r][c] == "#"
                or board[r][c] not in trie_node.children
            ):
                return

            prev = trie_node
            trie_node = trie_node.children[board[r][c]]
            if trie_node.word_idx != -1:
                out.append(words[trie_node.word_idx])
                trie_node.word_idx = -1  # word added once need not be added again

            temp = board[r][c]
            board[r][c] = "#"
            dfs(r + 1, c, trie_node)
            dfs(r - 1, c, trie_node)
            dfs(r, c - 1, trie_node)
            dfs(r, c + 1, trie_node)
            board[r][c] = temp

            # cleanup post-order
            if trie_node.word_idx == -1 and not trie_node.children:
                del prev.children[board[r][c]]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, word_trie.root)

        return out
