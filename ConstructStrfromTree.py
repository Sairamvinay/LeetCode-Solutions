class TreeNode(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def tree2str(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        elif root.left is None and root.right is None:
            return  str(root.val) 
        
        else:
            S = ""
            S += str(root.val)
                
            left = self.tree2str(root.left)
            if left != "()" :
                S +=   "(" + left + ")"
            
            
            
            right =  self.tree2str(root.right)
            if right != "()" and right != "":
                S +=   "(" + right + ")"
            
            
            
            return S
