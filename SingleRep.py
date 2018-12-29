class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        D = {}
        for n in nums:
            if n not in D:
                D[n] = 1
            
            else:
                D[n] += 1
        
        for k in D:
            if D[k] == 1:
                return k
