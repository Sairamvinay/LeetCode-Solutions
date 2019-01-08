# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def all_leaves(self,root):
        if root == None:
            return []
        
        elif root.right == None and root.left == None:
            return [root.val]
        else:
           
            return self.all_leaves(root.right) + self.all_leaves(root.left)
            
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.all_leaves(root1) == self.all_leaves(root2)
        
       
