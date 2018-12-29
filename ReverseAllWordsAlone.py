class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = s.split(" ")
        S = ''
        for word in L:
            S += word[::-1] + ' '
            
        
        
        return S.rstrip()
