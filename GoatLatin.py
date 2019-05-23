class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        S = ''
        addthru = "maa"
        for word in words:
            if word[0].lower() in "aeiou":
                S += word + addthru + ' '
                addthru += 'a'
            
            else:
                S += word[1::] + word[0] + addthru + ' '
                addthru += 'a'
        
        
        return S.rstrip()
                
