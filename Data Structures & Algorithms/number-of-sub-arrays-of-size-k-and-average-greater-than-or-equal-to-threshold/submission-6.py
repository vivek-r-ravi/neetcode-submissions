# brute force
# O(n*k) time, O(1) space
class SolutionV1:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        out = 0
        for L in range(n - k + 1):
            sub_sum = 0
            for R in range(L, L + k):
                if R - L + 1 < k:
                    sub_sum += arr[R]
                if R - L + 1 == k:
                    sub_sum += arr[R]
                    if sub_sum / k >= threshold:
                        out += 1
        return out


# sliding window
# O(n) time, O(1) space
# further optimized by comparing sum to threshold*k instead of division operation
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        sub_sum = 0
        L = 0
        out = 0
        for R in range(n):
            if R - L + 1 < k:
                sub_sum += arr[R]
            if R - L + 1 == k:
                sub_sum += arr[R]
                if sub_sum / k >= threshold:
                    out += 1
                sub_sum -= arr[L]
                L += 1
        return out
