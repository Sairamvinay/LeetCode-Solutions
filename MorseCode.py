class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        VIVEGAM = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        D = {}
        for word in words:
            word = word.lower()
            morse = ""
            for c in word:
                morse += VIVEGAM[ord(c) - ord('a')]
            
            if morse not in D:
                D[morse] = 1
            
            else:
                
                D[morse] = D[morse] + 1
        
        return len(D)
