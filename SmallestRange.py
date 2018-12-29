class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = min(A)
        M = max(A)
        return max(M - m - (2*K),0)
