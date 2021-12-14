# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal,maxVal = min(p.val,q.val), max(p.val, q.val)
        while(root.val != minVal and root.val != maxVal):
            if root.val > minVal and root.val < maxVal:
                return root
            if root.val > maxVal:
                root = root.left
            elif root.val < minVal:
                root = root.right
                
        return root