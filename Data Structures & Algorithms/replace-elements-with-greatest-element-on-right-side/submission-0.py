class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        # solution 1: brute force array traversing O(n2)
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i]=-1
            else:
                arr[i]=arr[i+1]
                for j in range(i+1,len(arr)):
                    arr[i]=max(arr[i],arr[j])
        return arr
        '''

        '''
        # solution 2: array traversing with max function O(n2)
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i]=-1
            else:
                arr[i]=max(arr[i+1:])
        return arr
        '''

        # solution 3: array traversing while maintaining max value O(n)
        best = arr[-1]
        for i in range(-1,-len(arr)-1,-1):
            if i==-1:
                arr[i]=-1
            else:
                curr=arr[i]
                arr[i]=best
                best=max(curr,best)
        return arr