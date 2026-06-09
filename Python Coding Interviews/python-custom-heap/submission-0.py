import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = [] # stores tuples of (-num, num)

    for num in nums:
        pair = (-num, num)
        heapq.heappush(max_heap, pair)

    result = []
    while max_heap:
        pair = heapq.heappop(max_heap)
        original = pair[1]
        result.append(original)
    
    return result


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
