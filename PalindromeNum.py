class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = abs(x)
        
        if x < 0:
            return False
        
        else:
            rev = 0
            while n != 0:
                rem = n % 10
                rev = (rev*10) + rem
                n = n // 10

            
            return (rev == x)
                
