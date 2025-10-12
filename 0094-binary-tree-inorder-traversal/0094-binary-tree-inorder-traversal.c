/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void recursive(struct TreeNode* root, int * array, int * i) {
    if (!root) {
        return;
    }
    recursive(root->left, array, i);    
    array[*i] = root->val;
    (*i)++;
    recursive(root->right, array, i);    
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    
    int * output = malloc(100 * sizeof(int));
    int i = 0;
    recursive(root, output, &i);
    *returnSize = i;
    return output;
}
