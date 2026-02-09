/*
 * Solution for Challenge 4: Binary Tree Cameras
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

int camerasCount;
const int NOT_COVERED = 0, HAS_CAMERA = 1, COVERED_STATE = 2;
int dfs(TreeNode* node) {
    if (!node) return COVERED_STATE;
    int left = dfs(node->left);
    int right = dfs(node->right);
    if (left == NOT_COVERED || right == NOT_COVERED) { camerasCount++; return HAS_CAMERA; }
    if (left == HAS_CAMERA || right == HAS_CAMERA) return COVERED_STATE;
    return NOT_COVERED;
}
int solve(TreeNode* root) {
    camerasCount = 0;
    if (dfs(root) == NOT_COVERED) camerasCount++;
    return camerasCount;
}

int main() { return 0; }
