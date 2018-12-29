class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        D = {}
        for candy in candies:
            if candy not in D:
                D[candy] = 1
            
            else:
                pass
        
        half = len(candies) / 2
        diff = len(D)
        return min(half,diff)
            
            
        
