class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good=""
        for L in range(len(num)-2):
            if num[L]==num[L+1]==num[L+2]:
                max_good=max(max_good,"".join([num[L],num[L+1],num[L+2]]))
        return max_good