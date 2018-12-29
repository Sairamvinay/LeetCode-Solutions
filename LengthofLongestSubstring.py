class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr =str()
        result = []
        for i in range(0,len(s)):
            
            if s[i] not in substr:
                substr += s[i]
            
            else:
                result.append(len(substr))
                for j in range(len(substr)):
                    if s[i] == substr[j]:
                        break
                
                substr = substr[j+1:]
                substr += str(s[i])
         
        result.append(len(substr))      
             
            
        maxl = max(result)
                
        
        return maxl
                
