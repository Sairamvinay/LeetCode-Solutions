class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum = 0
        valids = []
        for op in ops:
            
            if op.isdigit() or op[0] == '-':
               
                if op[0] == '-':
                    val = -1 * int(op[1:])
                else:
                     val = int(op)
                        
                sum += val
                valids.append(val)
            
            elif op == "C":
                sum -= valids.pop()
            
            elif op == "D":
                sum += (2*valids[-1])
                valids.append(valids[-1] * 2)
            
            else:
                sum += valids[-1] + valids[-2]
                valids.append(valids[-1] + valids[-2])
        
        
        return sum
