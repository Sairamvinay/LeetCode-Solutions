class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for i in range(len(A[0])):
            tmp = []
            for j in range(len(A)):
                tmp.append(A[j][i])
            
            B.append(tmp)
        
        
        return B
