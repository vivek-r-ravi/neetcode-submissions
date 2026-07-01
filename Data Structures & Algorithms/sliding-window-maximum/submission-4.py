# check max every time in sliding window
# O(n*k) time and O(k) space
class SolutionV1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        out = []
        l = 0
        for r in range(len(nums)):
            if r - l + 1 < k:
                window.append(nums[r])
            elif r - l + 1 == k:
                window.append(nums[r])
                out.append(max(window))
                window.popleft()
                l += 1
        return out


# maintain max heap
# O(nlogn) time and O(n) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        out = []
        l = 0
        for r in range(len(nums)):
            if r - l + 1 < k:
                heapq.heappush_max(max_heap, (nums[r], r))
            elif r - l + 1 == k:
                heapq.heappush_max(max_heap, (nums[r], r))
                while max_heap[0][1] < l:
                    heapq.heappop_max(max_heap)
                out.append(max_heap[0][0])
                l += 1
        return out
