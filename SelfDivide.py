class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if 1 <= left <= right and right <= 9:
            return range(left,right + 1,1)
        
        
        else:
            L = []
            for num in range(left,right + 1):
                
                
                if num % 10 == 0:
                    continue
                else:
                    num2 = int(num)    
                    isSelf = True
                    l = list(str(num2))
                    if "0" in l:
                        continue
                    else:
                        while num2 > 0:
                            dig = num2 % 10
                            num2 /= 10
                            if num % dig != 0:
                                isSelf = False
                                break
                        
                        if isSelf == True:
                            L.append(num)
            return L
                
