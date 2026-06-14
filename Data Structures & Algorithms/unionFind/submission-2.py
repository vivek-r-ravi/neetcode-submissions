# O(α(n)) time for find, isSameComponent, union
# O(1) time for getNumComponents
# O(n) space
class UnionFind:
    
    def __init__(self, n: int):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
        self.num_components=n

    def find(self, x: int) -> int:
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return self.par[x]
        
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)

    def union(self, x: int, y: int) -> bool:
        p,q=self.find(x),self.find(y)
        if p==q:
            return False
        if self.rank[p]>self.rank[q]:
            self.par[q]=p
        elif self.rank[p]<self.rank[q]:
            self.par[p]=q
        else:
            self.par[p]=q
            self.rank[q]+=1
        self.num_components -= 1
        return True        

    def getNumComponents(self) -> int:
        return self.num_components