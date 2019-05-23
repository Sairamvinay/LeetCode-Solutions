class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        D = {}
        for S in strs:
            key = list(S)
            key.sort()
            K = tuple(key)
            if K not in D:
                D[K] = [S]
            
            else:
                D[K].append(S)
        
        return D.values()
        
