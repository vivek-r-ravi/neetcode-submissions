# brute force: find max left and right height for each index
# O(n2) time O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        out=0
        for i in range(1,n-1):
            l=0
            for j in range(i):
                if height[j]>height[l]:
                    l=j
            r=len(height)-1
            for k in range(i+1,n):
                if height[k]>height[r]:
                    r=k
            vol=min(height[l],height[r])-height[i]
            out+=vol if vol>0 else 0
        return out         