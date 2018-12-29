class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        indices = []
        binary = bin(N)
        for index in range(len(binary)):
            if binary[index] == "1":
                indices.append(index)
        
        
        if len(indices) < 2:
            return 0
        
        M = 0

        for i in range(len(indices) - 1):
            
            if M < (indices[i+1] - indices[i]):
                M = (indices[i+1] - indices[i])
            
            
        return M            
