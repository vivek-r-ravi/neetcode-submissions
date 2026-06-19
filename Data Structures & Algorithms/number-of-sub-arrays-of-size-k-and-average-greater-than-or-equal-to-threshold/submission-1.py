# sliding window
# O(n) time, O(k) space
class SolutionV1:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        sub_sum=sum(arr[:k])
        L=0
        out=1 if sub_sum/k>=threshold else 0
        for R in range(k,n):
            sub_sum+=arr[R]-arr[L]
            L+=1
            if sub_sum/k>=threshold:
                out+=1
        return out


# sliding window
# O(n) time, O(1) space
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        sub_sum=0
        L=0
        out=0
        for R in range(n):
            if R-L+1<k:
                sub_sum+=arr[R]
            if R-L+1==k:
                sub_sum+=arr[R]
                if sub_sum/k>=threshold:
                    out+=1
                sub_sum-=arr[L]
                L+=1
        return out
