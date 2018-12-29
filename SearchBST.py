class TreeNode(object):

    def __init__(self,x):

        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        elif val == root.val:
            return root
        
        elif val < root.val:
            return self.searchBST(root.left,val)
        
        else:
            return self.searchBST(root.right,val)
        
