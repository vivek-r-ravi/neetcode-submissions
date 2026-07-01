class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev_small = [-1]*n
        next_small = [n]*n
        stack = []
        for i,height in enumerate(heights):
            while stack and stack[-1][0]>height:
                _, idx = stack.pop()
                next_small[idx] = i
            stack.append((height,i))
        stack = []
        for i,height in enumerate(heights):
            while stack and stack[-1][0]>=height:
                stack.pop()
            prev_small[i] = stack[-1][1] if stack else prev_small[i]
            stack.append((height,i))
        print(prev_small)
        print(next_small)
        max_h = 0
        for i,height in enumerate(heights):
            max_h = max(max_h,height*(next_small[i]-prev_small[i]-1))
        return max_h