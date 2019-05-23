class Solution(object):
    def match(self,L):
        if len(L) == 2:
            return -1 * int(L[1])
        
        else:
            return int(L[0])
        
    
    
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        comp1 = a.split('+')
        comp2 = b.split('+')
        L1 = comp1[0].split('-')
        L2 = comp1[1][:comp1[1].find('i'):].split('-')
        L3 = comp2[0].split('-')
        L4 = comp2[1][:comp2[1].find('i'):].split('-')
        real1 = self.match(L1)
        img1 = self.match(L2)
        real2 = self.match(L3)
        img2 = self.match(L4)
        
        Rprd = str((real1 * real2) - (img1 * img2))
        Iprd = str((real1 * img2) + (real2 * img1)) + 'i'
        return Rprd + '+' +Iprd
        
        
    
