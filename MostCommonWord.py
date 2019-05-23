from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(',',' ')
        words = paragraph.split(' ')
        wordCounter = Counter()
        print words
        for word in words:
            if word:
                word = word.strip(' ')
                word = word.strip(".,!?';")
                wordCounter[word] += 1
        
        max_v = -1 * (2**31)
        word = ''
        
        for k in wordCounter:
            if wordCounter[k] > max_v and k not in banned:
                word = k
                max_v = wordCounter[k]
        
        return word
        
