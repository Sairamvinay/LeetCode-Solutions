class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        D = dict()
        for num in A:
            if num in D:
                return num
            
            else:
                D[num] = 1
        
