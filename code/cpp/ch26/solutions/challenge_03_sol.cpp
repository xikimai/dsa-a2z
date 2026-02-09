/*
 * Solution for Challenge 3: Boundary Traversal
 * Chapter 26: Trees — Branches of Logic
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_map>
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

bool isLeaf(TreeNode* node) {
    return node && !node->left && !node->right;
}
void addLeaves(TreeNode* node, vector<int>& result) {
    if (!node) return;
    if (isLeaf(node)) { result.push_back(node->val); return; }
    addLeaves(node->left, result);
    addLeaves(node->right, result);
}
vector<int> solve(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    if (isLeaf(root)) return {root->val};
    result.push_back(root->val);
    // Left boundary
    TreeNode* node = root->left;
    while (node) {
        if (!isLeaf(node)) result.push_back(node->val);
        node = node->left ? node->left : node->right;
    }
    // Leaves
    addLeaves(root, result);
    // Right boundary (reversed)
    vector<int> rightBound;
    node = root->right;
    while (node) {
        if (!isLeaf(node)) rightBound.push_back(node->val);
        node = node->right ? node->right : node->left;
    }
    for (int i = rightBound.size() - 1; i >= 0; i--) result.push_back(rightBound[i]);
    return result;
}

int main() { return 0; }
