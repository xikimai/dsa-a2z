/*
 * Solution for Practice 7: Maximum Path Sum
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

int maxPathSumVal;
int maxGain(TreeNode* node) {
    if (!node) return 0;
    int left = max(maxGain(node->left), 0);
    int right = max(maxGain(node->right), 0);
    maxPathSumVal = max(maxPathSumVal, left + right + node->val);
    return node->val + max(left, right);
}
int solve(TreeNode* root) {
    maxPathSumVal = INT_MIN;
    maxGain(root);
    return maxPathSumVal;
}

int main() { return 0; }
