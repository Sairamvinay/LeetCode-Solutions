class Solution(object):
    def removeOccurrences(self,e):
        return list(set(e))
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = self.removeOccurrences(nums)
        if len(nums) < 3:
            return max(nums)
        
        else:
            
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
