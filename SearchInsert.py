class Solution(object):
    def BSearch(self,nums,target,start,end):
        mid = (start + end)/2
        while start <= end:
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return self.BSearch(nums,target,mid+1,end)
            
            else:
                return self.BSearch(nums,target,start,mid-1)
            
        
        
    
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return self.BSearch(nums,target,0,len(nums))
        
        else:
            if nums[0] > target:
                return 0
            elif nums[-1] < target:
                return len(nums) 
            
            else:
                for i in range(len(nums) - 1):
                    if (nums[i] < target) and (target < nums[i+1]):
                        return i+1
