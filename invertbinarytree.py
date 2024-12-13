from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Function to build a binary tree from a list (level-order representation)
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        head = root
        # Recursion is going to be the easiest I think
        # Base Case: when you have reached the end of the tree, and the node has no more children
        
        if not root:
            return
        
        dummy = root.left
        root.left = root.right
        root.right = dummy
        
        Solution().invertTree(root.left)
        Solution().invertTree(root.right)

        return head

# Function to print the binary tree in level-order (to verify the output)
def print_tree(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for clarity
    while result and result[-1] is None:
        result.pop()

    return result

# Test the invertTree function
if __name__ == "__main__":
    # Input tree: [4,2,7,1,3,6,9]
    input_tree = [4,2,7,1,3,6,9]
    root = build_tree(input_tree)

    # Invert the binary tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Output the inverted tree as a list
    output_tree = print_tree(inverted_root)
    print("Output:", output_tree)
