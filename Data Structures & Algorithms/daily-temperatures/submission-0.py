# brute force
# O(n2) time
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[]
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    break
            if len(result)!=i+1:
                result.append(0)
        return result
