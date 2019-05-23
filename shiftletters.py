class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shift_new = 0
        S_result = ''
        Sums = sum(shifts)
        shift = Sums % 26
        for i in range(len(shifts)):
            shift_new = shift % 26
            if (shift_new + ord(S[i])) > 122:
                S_result += chr(97 + shift_new - (122 - ord(S[i])) - 1)
                shift -= shifts[i]
                
            
            else:
                S_result += chr(shift_new + ord(S[i]))
                shift -= shifts[i]
            
            
                
            
