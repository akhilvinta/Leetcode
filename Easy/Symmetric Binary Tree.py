# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)
        
    def helper(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 and t2:
            return t1.val == t2.val and self.helper(t1.left, t2.right)\
                and self.helper(t1.right, t2.left)
        if (t1 and not t2) or (t2 and not t1):
            return False
    
        return True