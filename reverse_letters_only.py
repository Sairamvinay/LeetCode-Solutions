class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = ''
        for c in S:
            if c.isalpha():
                letters += c
         
        result = ''
        letters = letters[::-1]
        j= 0 
        for i in range(len(S)):
            if not S[i].isalpha():
                result += S[i]
            
            else:
                result += letters[j]
                j += 1
        
        return result
