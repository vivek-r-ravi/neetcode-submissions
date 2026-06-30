class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {num: i for i, num in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                top = stack.pop()
                if top in nums1_map:
                    ans[nums1_map[top]] = nums2[i]
            stack.append(nums2[i])
        return ans
