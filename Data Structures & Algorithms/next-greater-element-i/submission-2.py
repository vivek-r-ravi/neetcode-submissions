'''
Problem:
The next greater element of some element x in an array is the first greater element 
that is to the right of x in the array.

You are given two 0-indexed integer arrays nums1 and nums2.
nums1 is a subset of nums2. Both contain unique elements.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j].
Then, determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
'''

# monotonic stack solution
# O(n1+n2) time and O(n1) space
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {num: i for i, num in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                top = stack.pop()
                ans[nums1_map[top]] = nums2[i]
            if nums2[i] in nums1_map:
                stack.append(nums2[i])
        return ans
