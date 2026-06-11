# naive solution: counter dictionary + sorting using value
# O(nlogn) time and O(n) space
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num[0] for num in sorted(Counter(nums).items(),key=lambda x: x[1], reverse=True)[:k]]