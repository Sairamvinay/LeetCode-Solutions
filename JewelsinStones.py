class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = dict()
        for i in range(len(S)):
            if S[i] in d:
                d[S[i]] += 1
            else:
                d[S[i]] = 1
        
       # print d
        s = 0
        for j in range(len(J)):
            if J[j] in d:
                s+= d[J[j]]
        
        return s
