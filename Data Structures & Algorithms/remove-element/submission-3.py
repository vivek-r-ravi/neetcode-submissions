class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # do not create another array, so use the same array
        
        # solution 1: brute force pythonic way O(n) time and space
        # even though new array not created, internally additional memory consumed
        '''
        nums[:] = [i for i in nums if i!=val]
        k = len(nums)
        '''
        
        # solution 2: efficient two pointers O(n) time and O(1) space 
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        '''

        # solution 3: efficient two pointers with less operations
        i = 0
        k = len(nums)
        while i<k:
            if nums[i]==val:
                nums[i]=nums[k-1]
                k-=1
            else:
                i+=1

        return k