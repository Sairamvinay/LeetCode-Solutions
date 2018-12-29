class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        direc = path.split("/")
        L = []
        end = 0
        if len(direc) == 1 and direc[0] == "..":
            return "/"
        for i in range(len(direc)):
            if direc[i] != "" and direc[i] != ".":
                if direc[i] == "..":
                    end+= 1
                    if L == []: #edge case when first encountering a .. do nothing and skip
                        pass
                    else:
                        L.pop()
                else:
                    L.append(direc[i])
        
        return "/" + "/".join(L)
                
