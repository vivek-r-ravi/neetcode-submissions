# brute force
# O(n2) time O(1) space
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    break
            if len(result) != i + 1:
                result.append(0)
        return result


# monotonic stack
# O(n2) time O(1) space
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                _, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temp, i))
        return result
