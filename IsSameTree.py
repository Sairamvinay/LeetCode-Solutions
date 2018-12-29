class TreeNode(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x

class Solution(object):
    def preorder(self,root):
        if root is None:
            return [None]
        
        if ((root.left is None) and (root.right is None)):
            return [root.val]
        
        else:
            L = []
            L.append(root.val)
            L += self.preorder(root.left)
            L += self.preorder(root.right)
            return L
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self.preorder(p) == self.preorder(q)
