class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        D = {}
        uncommon = []
        L = A.split()
        M = B.split()
        for word in (L+M):
            if word in D:
                D[word] += 1
            
            else:
                D[word] = 1
        
        for key in D:
            if D[key] == 1:
                uncommon.append(key)
        
        
        return uncommon
