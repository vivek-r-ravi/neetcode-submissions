# Binary Search Tree Node
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:

        def insert_helper(node, key, val):
            if not node:
                return TreeNode(key, val)
            if node.key == key:
                node.val = val
            elif node.key > key:
                node.left = insert_helper(node.left, key, val)
            else:
                node.right = insert_helper(node.right, key, val)
            return node

        self.root = insert_helper(self.root, key, val)

    def get(self, key: int) -> int:

        def get_helper(node, key):
            if not node:
                return -1
            if node.key == key:
                return node.val
            elif node.key > key:
                return get_helper(node.left, key)
            else:
                return get_helper(node.right, key)

        return get_helper(self.root, key)

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:

        def remove_helper(node, key):
            if not node:
                return

            if node.key > key:
                node.left = remove_helper(node.left, key)
            elif node.key < key:
                node.right = remove_helper(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    in_order_successor = min_key_node(node.right)
                    in_order_successor.left = node.left
                    return node.right
            return node

        def min_key_node(node):
            if not node:
                return None

            while node.left:
                node = node.left
            return node

        self.root = remove_helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        out = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            out.append(node.key)
            inorder(node.right)

        inorder(self.root)
        return out
