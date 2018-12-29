class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = sorted(nums)[::2] # because we need to get hold of all even indices such that it serves as the minimal element
        return sum(N)
