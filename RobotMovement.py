class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        D = {"U" : (0,1), "D": (0,-1) , "R":(1,0) , "L":(-1,0)}
        x = 0
        y = 0
        for move in moves:
            move = move.upper() #neglect issues
            x += D[move][0]
            y += D[move][1]
        
        return (x == 0 and y == 0)
