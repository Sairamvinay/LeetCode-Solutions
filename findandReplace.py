class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        Matcher = []
        for word in words:
            D = {}
            for i in range(len(word)):
                addit = True
                if pattern[i] in D:
                    if D[pattern[i]] != word[i]:
                        addit = False
                        break
                    
                    else:
                        pass
                
                else:
                    if word[i] in D.values():
                        addit = False
                        break
                    
                    else:
                        D[pattern[i]] = word[i]
            
            if addit:
                Matcher.append(word)
        
        
        return Matcher
