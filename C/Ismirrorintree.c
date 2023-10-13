#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct TreeNode TreeNode;

bool isMirror(TreeNode* left, TreeNode* right) {
    if (left == NULL && right == NULL) {
        return true;
    }
    if (left == NULL || right == NULL) {
        return false;
    }
    return (left->val == right->val) &&
           isMirror(left->left, right->right) &&
           isMirror(left->right, right->left);
}

bool isSymmetric(TreeNode* root) {
    if (root == NULL) {
        return true;
    }
    return isMirror(root->left, root->right);
}

int main() {
    // Create a sample binary tree (symmetric):
    //         1
    //        / \
    //       2   2
    //      / \ / \
    //     3  4 4  3

    // Create tree nodes
    TreeNode* node1 = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node2a = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node2b = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node3a = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node4a = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node3b = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* node4b = (TreeNode*)malloc(sizeof(TreeNode));

    // Initialize tree nodes
    node1->val = 1;
    node2a->val = 2;
    node2b->val = 2;
    node3a->val = 3;
    node4a->val = 4;
    node3b->val = 3;
    node4b->val = 4;

    // Connect nodes to form the symmetric tree
    node1->left = node2a;
    node1->right = node2b;
    node2a->left = node3a;
    node2a->right = node4a;
    node2b->left = node4b;
    node2b->right = node3b;
    node3a->left = node3a->right = node4a->left = node4a->right = node3b->left = node3b->right = node4b->left = node4b->right = NULL;

    // Check if the tree is symmetric and print the result
    if (isSymmetric(node1)) {
        printf("true\n");
    } else {
        printf("false\n");
    }

    // Free dynamically allocated memory
    free(node1);
    free(node2a);
    free(node2b);
    free(node3a);
    free(node4a);
    free(node3b);
    free(node4b);

    return 0;
}
