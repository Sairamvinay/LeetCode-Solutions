class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        deleted = ""
        for c in range(len(s)):
            
            if s[c] in d:
                del d[s[c]]
                deleted += s[c]
                continue
            
            elif s[c] in deleted:
                continue
            
            else:
                
                d[s[c]] = c
        
        
        if d == {}:
            return -1
        
        return min(d.values())
        
