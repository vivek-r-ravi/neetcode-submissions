# naive solution: counter dictionary + sorting using value
# O(nlogn) time and O(n) space
class SolutionV1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [
            num[0] for num in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[:k]
        ]


# canonical solution: counter dictionary + min heap
# O(nlogk) time and O(n+k) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = [(x[1], x[0]) for x in Counter(nums).items()]
        heap = []
        for count_num in count_nums:
            if len(heap) < k:
                heapq.heappush(heap, count_num)
            else:
                heapq.heappushpop(heap, count_num)
        return [y[1] for y in heap]
