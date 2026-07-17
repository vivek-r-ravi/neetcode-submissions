# backtracking
# O(n*n!) time O(n) space
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


# backtracking with permutations in place
# O(n*n!) time O(1) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out= []

        def dfs(i):
            if i == len(nums):
                out.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i+1)
                nums[j], nums[i] = nums[i], nums[j]

        dfs(0)
        return out
