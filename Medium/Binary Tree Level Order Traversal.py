# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class nodeAndLevel:
    def __init__(self, root, level):
        self.root = root
        self.level = level
        
    def __str__(self):
        return str(self.root) + ", " + str(self.level)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        queue = []
        dict = {}
        queue.append(nodeAndLevel(root,0))

        while queue:
            if queue[0].level not in dict:
                dict[queue[0].level] = [queue[0].root.val]
            else:
                dict[queue[0].level].append(queue[0].root.val)
            if queue[0].root.left:
                queue.append(nodeAndLevel(queue[0].root.left, queue[0].level + 1))
            if queue[0].root.right:
                queue.append(nodeAndLevel(queue[0].root.right, queue[0].level + 1))
            queue.pop(0)
        
        retList = []
        for key in sorted(dict):
            retList.append(dict[key])
                
        return retList

            