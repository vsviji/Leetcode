class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirror(root.left, root.right);
    }

    public boolean isMirror(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        return (left.val == right.val) &&
               isMirror(left.left, right.right) &&
               isMirror(left.right, right.left);
    }

    public static void main(String[] args) {
        // Create a sample binary tree (symmetric):
        //         1
        //        / \
        //       2   2
        //      / \ / \
        //     3  4 4  3

        // Create tree nodes
        TreeNode node1 = new TreeNode(1);
        TreeNode node2a = new TreeNode(2);
        TreeNode node2b = new TreeNode(2);
        TreeNode node3a = new TreeNode(3);
        TreeNode node4a = new TreeNode(4);
        TreeNode node3b = new TreeNode(3);
        TreeNode node4b = new TreeNode(4);

        // Connect nodes to form the symmetric tree
        node1.left = node2a;
        node1.right = node2b;
        node2a.left = node3a;
        node2a.right = node4a;
        node2b.left = node4b;
        node2b.right = node3b;

        // Create an instance of the Solution class
        Solution solution = new Solution();

        // Check if the tree is symmetric and print the result
        System.out.println(solution.isSymmetric(node1)); // This should print "true"
    }
}
