# brute force: find max left and right height for each index
# O(n2) time O(1) space
class SolutionV1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        out = 0
        for i in range(1, n - 1):
            l = 0
            for j in range(i):
                if height[j] > height[l]:
                    l = j
            r = len(height) - 1
            for k in range(i + 1, n):
                if height[k] > height[r]:
                    r = k
            vol = min(height[l], height[r]) - height[i]
            out += vol if vol > 0 else 0
        return out


# prefix and suffix max arrays
# O(n) time O(n) space
class SolutionV2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        out = 0
        prefix_max = [0] * n
        suffix_max = [0] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i + 1])
        for i in range(1, n - 1):
            vol = min(prefix_max[i], suffix_max[i]) - height[i]
            out += vol if vol > 0 else 0
        return out


# canonical solution: two pointers (space compression of above)
# O(n) time O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        out = 0
        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                out += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                out += right_max - height[r]
        return out
