class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        L1 = version1.split(".")
        L2 = version2.split(".")
        
        eq = 0
        for i in range(min(len(L1), len(L2))):
            if int(L1[i]) < int(L2[i]):
                return -1
                
            elif int(L1[i]) > int(L2[i]):
                return 1
                
            else:
                eq = 1

        if eq == 1:
            if len(L1) > len(L2):
                for j in range(len(L2),len(L1)):
                    if int(L1[j]) != 0:
                        return 1
            
            elif len(L1) < len(L2):
                for j in range(len(L1),len(L2)):
                    if int(L2[j]) != 0:
                        return -1
        
            
        return 0
