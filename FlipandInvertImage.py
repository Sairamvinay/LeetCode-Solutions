class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for rows in A:
            rows.reverse()
            
            for item in range(len(rows)):
                rows[item] ^= 1
            
            
        
        return A
