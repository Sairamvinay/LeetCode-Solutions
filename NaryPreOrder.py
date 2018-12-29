class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        elif root.children == []:
            return [root.val]
        
        else:
            L = []
            L.append(root.val)
            for c in root.children:
                L = L + self.preorder(c)
                
            return L
        
