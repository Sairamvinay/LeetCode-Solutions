class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children




class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        
        else:
            
            depth = []
            for c in root.children:
                depth.append(self.maxDepth(c))
            
            if depth == []:
                return 1
            else:
                return 1+max(depth)
