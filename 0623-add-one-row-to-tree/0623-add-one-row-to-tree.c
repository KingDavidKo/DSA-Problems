/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if (!root) {
        return NULL;
    } else if (depth == 1) {
        struct TreeNode * lnode = malloc(sizeof(struct TreeNode));
        lnode->left = root;
        lnode->val = val;
        lnode->right = NULL;
        return lnode;
    } else if (depth == 2) {
        struct TreeNode * lnode = malloc(sizeof(struct TreeNode));
        struct TreeNode * rnode = malloc(sizeof(struct TreeNode));
        lnode->val = val;
        lnode->left = root->left;
        lnode->right = NULL;

        rnode->val = val;
        rnode->right = root->right;
        rnode->left = NULL;

        root->left = lnode;
        root->right = rnode;
        return root;
    }  else {
        root->left = addOneRow(root->left, val, depth - 1);
        root->right = addOneRow(root->right, val, depth - 1);
        return root;
    }    
    
}