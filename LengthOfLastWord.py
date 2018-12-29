class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        L = s.split(' ')
        print L
        if len(L) == 1:
            return len(L[0])
        
        return len(L[-1])
