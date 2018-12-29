class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        total = 0
        lineno = 1
        for s in S.lower():
            total += widths[ord(s) - ord('a')]
            if total > 100:
                lineno += 1
                total = widths[ord(s) - ord('a')]
            
        
        return [lineno,total]
        
        
