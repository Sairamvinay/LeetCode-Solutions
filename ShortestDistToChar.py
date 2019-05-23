class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        find = S.find(C)
        dist = []
        finds = []
        prev_find = S.find(C)
        for i in range(len(S)):
            find = S.find(C,i,len(S))
            if find not in finds:
                if finds != []:
                    prev_find = finds[-1]
                    
                finds.append(find)
            
            
            dist.append(min(abs(i - find),abs(i - prev_find)))
            
            
        return dist
