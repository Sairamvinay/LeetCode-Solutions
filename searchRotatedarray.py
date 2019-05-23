class Solution(object):
    def helper(self,low,high,nums,target):
        
        if low >= high:
            if nums[low] == target:
                return low
            
            else:
                return -1
        
        else:
            middle = (low + high) / 2
            left = self.helper(low,middle,nums,target)
            right = self.helper(middle + 1,high,nums,target)
            if left != -1:
                return left

            if right != -1:
                return right

            else:
                return -1
            
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1 
        if nums == []:
            return -1
        else:
            return self.helper(low,high,nums,target)
        
        
