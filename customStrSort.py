class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ''
        count = {}
        for c in T:
            if c in count:
                count[c] += 1
            
            else:
                count[c] = 1
        
        
        for c in S:
            if c not in T:
                pass
            else:
                ans += (c * count[c])
        
        
        for key in count:
            if key not in S:
                ans += count[key]*key
        
        return ans
