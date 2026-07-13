"""
Design a Disjoint Set (aka Union-Find) class.

Your UnionFind class should support the following operations:

* UnionFind(int n) will initialize a disjoint set of size n.
* int find(int x) will return the root of the component that x belongs to.
* bool isSameComponent(int x, int y) will return whether x and y belong to the same component.
* bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.
* int getNumComponents() will return the number of components in the disjoint set.
"""


# O(α(n)) time for find, isSameComponent, union due to union by rank and path compression
# O(1) time for getNumComponents
# O(n) space
class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.num_components = n

    def find(self, x: int) -> int:
        # path compression
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p, q = self.find(x), self.find(y)
        if p == q:
            return False
        # union by rank
        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[p] < self.rank[q]:
            self.par[p] = q
        else:
            self.par[p] = q
            self.rank[q] += 1
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
