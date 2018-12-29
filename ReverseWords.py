class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if "\t" in s:
            L = s.split("\t")
            
        L = s.split(" ")
        M = []
        for i in range(-1,-len(L) - 1,-1):
            if L[i] in " \t":
                pass
            else:
                M.append(L[i])
        
        S = " "
        return S.join(M)
        
