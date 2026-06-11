# naive solution: counter dictionary + sorting using value
# O(nlogn) time and O(n) space
from collections import Counter
class SolutionV1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num[0] for num in sorted(Counter(nums).items(),key=lambda x: x[1], reverse=True)[:k]]

# canonical solution: counter dictionary + min heap
# O(n+klogk) time and O(n) space
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums=[(x[1],x[0]) for x in Counter(nums).items()]
        heap=[]
        for count_num in count_nums:
            if len(heap)<k:
                heapq.heappush(heap,count_num)
            else:
                heapq.heappushpop(heap,count_num)
        return [x[1] for x in heap]