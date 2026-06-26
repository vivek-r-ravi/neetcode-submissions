class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1=len(s1)
        n_s2=len(s2)
        if n_s1>n_s2:
            return False
        
        count_s1=Counter(s1)
        count_s2=dict()
        l=0
        for r in range(n_s2):
            if r-l+1<=n_s1:
                count_s2[s2[r]]=count_s2.get(s2[r],0)+1
            if r-l+1==n_s1:
                print(count_s2)
                if count_s2==count_s1:
                    return True
                else:
                    count_s2[s2[l]]-=1
                    if count_s2[s2[l]]==0:
                        count_s2.pop(s2[l])
                    l+=1
        return False