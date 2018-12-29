class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = {"q" : 1,"w":1,"e":1,"r":1,"t":1,"y":1,"u":1,"i":1,"o":1,"p":1, "a":2,"s":2,"d":2,"f":2,"g":2,"h":2,"j":2,"k":2,"l":2,"z":3,"x":3,"v":3,"b":3,"n":3,"m":3,"c":3}
        
        wordsalike = []
        for word in words:
            same = True
            prev = 0
            for letter in word.lower():
                if prev == 0:
                    prev = rows[letter]
                
                if rows[letter] != prev:
                    same = False
                    break
            
            if same == True:
                wordsalike.append(word)
                
        
        return wordsalike
            
