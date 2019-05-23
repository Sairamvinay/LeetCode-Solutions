# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumthru(self, root,sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return -100000000
        
        elif root.right is None and root.left is None:
            return root.val
        
        else:
            S = root.val
            S1 = self.sumthru(root.left,sum - S)
            S2 = self.sumthru(root.right,sum - S)
            
            if (S + S1) == sum:
                return S + S1
            
            if (S + S2) == sum:
                return S + S2
            
          
            else:
                return -1000000
            
            
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        
        else:
            return self.sumthru(root,sum) == sum
        
