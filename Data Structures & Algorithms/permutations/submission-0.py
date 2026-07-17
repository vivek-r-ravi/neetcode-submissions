class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out, path, visited = [], [], set()

        def dfs():
            if len(path) == len(nums):
                out.append(path.copy())
                return

            for j in range(len(nums)):
                if j in visited:
                    continue
                path.append(nums[j])
                visited.add(j)
                dfs()
                visited.remove(j)
                path.pop()

        dfs()
        return out
