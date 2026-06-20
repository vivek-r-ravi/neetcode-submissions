class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def isTurbulent(L, R):
            if R - L + 1 == 1:
                return True
            if arr[R] == arr[R - 1]:
                return False
            if R - L + 1 == 2:
                return True
            if arr[R] > arr[R - 1] and arr[R - 1] > arr[R - 2]:
                return False
            if arr[R] < arr[R - 1] and arr[R - 1] < arr[R - 2]:
                return False
            return True

        n = len(arr)
        length = 0
        L = 0
        for R in range(n):
            if not isTurbulent(L, R):
                L = R - 1 if arr[R] != arr[R - 1] else R
            length = max(length, R - L + 1)
        return length
