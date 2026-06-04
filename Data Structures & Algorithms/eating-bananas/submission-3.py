class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # helper function to determine hours taken for a speed k
        def canFinish(k: int) -> bool:
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
                if hours>h:
                    return False
            return True

        # lower bound binary search on search range using helper function
        # find lowest k for which above function returns True
        # e.g: FFFFFTTTT
        left = 1
        right = max(piles)
        while left<=right:
            middle=(left+right)//2
            if canFinish(middle):
                right=middle-1
            else:
                left=middle+1
        return left