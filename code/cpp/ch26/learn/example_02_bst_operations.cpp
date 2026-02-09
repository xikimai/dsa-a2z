/*
 * Example 02: BST Operations — Search, Insert, Delete, Validate
 * Chapter 26: Trees — Branches of Logic
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* buildTree(vector<int> values, int null_val = INT_MIN) {
    if (values.empty() || values[0] == null_val) return nullptr;
    TreeNode* root = new TreeNode(values[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)values.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)values.size() && values[i] != null_val) {
            node->left = new TreeNode(values[i]);
            q.push(node->left);
        }
        i++;
        if (i < (int)values.size() && values[i] != null_val) {
            node->right = new TreeNode(values[i]);
            q.push(node->right);
        }
        i++;
    }
    return root;
}

TreeNode* bstSearch(TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    return target < root->val ? bstSearch(root->left, target) : bstSearch(root->right, target);
}

bool isValidBST(TreeNode* root, long lo = LONG_MIN, long hi = LONG_MAX) {
    if (!root) return true;
    if (root->val <= lo || root->val >= hi) return false;
    return isValidBST(root->left, lo, root->val) && isValidBST(root->right, root->val, hi);
}

void inorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);
    inorder(node->right, res);
}

int main() {
    TreeNode* bst = buildTree({4, 2, 6, 1, 3, 5, 7});
    vector<int> res;
    inorder(bst, res);
    cout << "BST inorder: [";
    for (int i = 0; i < (int)res.size(); i++) {
        if (i) cout << ",";
        cout << res[i];
    }
    cout << "]" << endl;
    cout << "Search 5: " << (bstSearch(bst, 5) ? "Found" : "Not found") << endl;
    cout << "Valid BST: " << (isValidBST(bst) ? "true" : "false") << endl;
    return 0;
}
