class Solution(object):
    def calcPow(self,x,n):
        if n == 0:
            return 1
        
        elif n == 1:
            return x
        
        else:
            res = self.calcPow(x,n/2)
            if n % 2 == 1:
                return res * res * x
            
            else:
                return res * res
        
        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0/float(x)
            n = abs(n)
    
        else:
            pass
        
        
        result = self.calcPow(x,n)
        return result
