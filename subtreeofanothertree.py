# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def build_tree(values):
    """
    Build a binary tree from a list of values in level-order.
    `None` values represent absent children.
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while i < len(values):
        current = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        if root == None: 
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

    def isSameTree(self, parent, child):
        if parent == None and child == None:
            return True
        
        if parent == None or child == None:
            return False

        if parent.val == child.val:
            return self.isSameTree(parent.left, child.left) and self.isSameTree(parent.right, child.right)
        
# Test case input
#root_values = [3, 4, 5, 1, 2]
root_values = [3,4,5,1,2,None,None,None,None,0]
subroot_values = [4, 1, 2]

# Build the trees
root = build_tree(root_values)
subRoot = build_tree(subroot_values)

# Testing the function
solution = Solution()
print(solution.isSubtree(root, subRoot))  # This will test your implementation.