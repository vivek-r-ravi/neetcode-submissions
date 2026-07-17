class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out, path, visited = [], [], set()

        def dfs():
            if len(path) == len(nums):
                out.append(path.copy())
                return

            for j in range(len(nums)):
                if j in visited:
                    continue
                if j > 0 and nums[j] == nums[j - 1] and j - 1 not in visited:
                    continue
                path.append(nums[j])
                visited.add(j)
                dfs()
                visited.remove(j)
                path.pop()

        dfs()
        return out


class SolutionV2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        def dfs(i):
            if i == len(nums):
                out.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        dfs(0)
        return out
