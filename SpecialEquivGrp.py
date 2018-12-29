from sets import Set
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D = Set()
        for str in A:
            ans = [0] * 52
            for i in range(len(str)):
                ans[ord(str[i]) - ord('a') + 26*(i%2)] += 1
            
            D.add(tuple(ans))
        
        return len(D)
