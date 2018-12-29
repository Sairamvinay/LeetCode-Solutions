class TreeNode(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
