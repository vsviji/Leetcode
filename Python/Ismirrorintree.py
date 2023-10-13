class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
# Create a sample binary tree (symmetric):
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3

# Create tree nodes
node1 = TreeNode(1)
node2a = TreeNode(2)
node2b = TreeNode(2)
node3a = TreeNode(3)
node4a = TreeNode(4)
node3b = TreeNode(3)
node4b = TreeNode(4)

# Connect nodes to form the symmetric tree
node1.left = node2a
node1.right = node2b
node2a.left = node3a
node2a.right = node4a
node2b.left = node4b
node2b.right = node3b

# Create an instance of the Solution class
solution = Solution()

# Check if the tree is symmetric and print the result
print(solution.isSymmetric(node1))  # This should print True
