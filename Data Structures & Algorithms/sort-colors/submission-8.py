# solution 1: use counting sort
# O(n+k) on time and O(k) on space
class SolutionV1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]  # for 0, 1, 2
        for num in nums:
            count[num] += 1
        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1


# solution 2: use counting sort (stable version) but needs aux array
# O(n+k) on time and O(n+k) on space
class SolutionV2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create count array
        count = [0, 0, 0]  # for 0, 1, 2
        for num in nums:
            count[num] += 1

        # prefix sum of count
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # overwrite original array from backward using aux
        aux = nums[:]
        for i in range(len(aux) - 1, -1, -1):
            current = aux[i]
            target_index = count[current] - 1
            nums[target_index] = current
            count[current] -= 1


# solution 3: Dutch National Flag solution using 3 pointers
# O(n) on time and O(1) on space
# class SolutionV3:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
