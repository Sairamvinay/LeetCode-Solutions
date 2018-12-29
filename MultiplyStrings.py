class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        L1 = num1[::-1]
        L2 = num2[::-1]
        n1 = 0
        n2 = 0
        i = 0
        j = 0
        for c in L1:
            
            n1 += (ord(c) - 48) * (10**i)
            i += 1
            
        for c in L2:
            n2 += (ord(c) - 48) * (10**j)
            j += 1
        
        return str(n1*n2)
        
        
        
