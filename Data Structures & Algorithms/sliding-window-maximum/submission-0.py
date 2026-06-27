class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=deque()
        out=[]
        l=0
        for r in range(len(nums)):
            if r-l+1<k:
                window.append(nums[r])
            elif r-l+1==k:
                window.append(nums[r])
                out.append(max(window))
                window.popleft()
                l+=1
        return out