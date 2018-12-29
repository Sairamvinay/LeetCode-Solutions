class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start = 0
        end = int(len(S))
        A = [0] * (end + 1)
        
        for i in range(len(S)):
            if S[i] == "I":
                A[i] = start
                start +=1
                
            
            elif S[i] == "D":
                A[i] = end
                end -=1
            
            else:
                 pass
        
        if S[-1] == "I":
            A[-1] = end
        
        else:
            A[-1] = start
            
        return A
