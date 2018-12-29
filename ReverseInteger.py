class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        n = abs(x)
        rev = 0
        while n!=0:
            rem = n%10
            n = n//10
            rev = rem + (rev*10)
                
        if x < 0:
            rev = rev * -1
        
        if rev > 2**31 or rev < -1*(2**31):
            return 0
        return rev
        
    
