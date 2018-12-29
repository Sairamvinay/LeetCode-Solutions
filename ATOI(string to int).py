class Solution(object):
    def myAtoi(self, S):
        """
        :type str: str
        :rtype: int
        """
        accept = [" ","+","-"]
        result = []
        for i in range(len(S)):
            
            if S[i] not in accept:
                if S[i].isdigit():
                    result.append(int(S[i]))
                else:
                    break
            
            elif S[i] == ' ':
                if len(result) >= 1:
                    break
                else:
                    pass
            
            elif S[i] == "+" or S[i] == '-':
                if '-' not in result and '+' not in result:
                    result.append(S[i])
                
                else:
                    break
            
            else:
                pass
        
        num = 0
        print result
        if result == []:
            return num
        
        else:
            start = 0
            attr = ""
            if result[0] == '-' or result[0] == "+":
                attr = result[0]
                start = 1
            
            for k in range(start,len(result)):
                if result[k] in range(0,10):
                    num = (num*10) + result[k]
                
                else:
                    return num
            
            if attr == "-":
                num = -1*num
                
            if num > (2**31 - 1):
                return 2**31 - 1                
            
            elif num < (-1 * (2**31)):
                return -1 * (2**31)
            
            else:
                return num
