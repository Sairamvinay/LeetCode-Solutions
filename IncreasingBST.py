class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorder(self,root):
        if root is None:
            return []
        
        L = []
        L += self.inorder(root.left)
        L += [root.val]
        L += self.inorder(root.right)
        return L
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = self.inorder(root)
        head = TreeNode(0)
        curr = head
        for val in inorder:
            
            curr.left = None
            curr.right = TreeNode(val)
            curr = curr.right
        
        return head.right
        
