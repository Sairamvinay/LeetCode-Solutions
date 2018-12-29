class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ''
        for i in str:
            if ord(i)>= 65 and ord(i) <= 91:
                s+= chr(ord(i) + 97 - 65)
            
            else:
                s+=i
        return s
            
