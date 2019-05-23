class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        op = []
        for i,v in enumerate(nums):
            ind = abs(v) - 1
            if nums[ind] < 0:
                op.append(abs(v))
            
            else:
                nums[ind] = -1 * nums[ind]
            
            
            
        
        return sorted(op)
                
