class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strings = []
        for i in range(1,n+1):
            if i % 15 == 0:
                
                strings.append("FizzBuzz")
            
            elif i % 3 == 0:
                strings.append("Fizz")
            
            
            elif  i % 5 == 0:
                strings.append("Buzz")
            
            
            else:
                strings.append(str(i))
        
        
        return strings
