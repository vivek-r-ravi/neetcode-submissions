class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def areBananasFinished(k: int) -> int:
            t=0
            for i in range(len(piles)):
                if piles[i]%k!=0:
                    t+=piles[i]//k+1
                else:
                    t+=piles[i]//k
                if t>h:
                    return -1
            return h

        # lower bound binary search
        # find highest k for which above function returns -1
        left = 1
        right = max(piles)
        while left<=right:
            middle=(left+right)//2
            if areBananasFinished(middle)==-1:
                left=middle+1
            else:
                right=middle-1
        return left