/*
 * Solution for Challenge 1: Construct from Preorder+Inorder
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

vector<int> treeToList(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        if (node) {
            result.push_back(node->val);
            q.push(node->left);
            q.push(node->right);
        } else {
            result.push_back(INT_MIN);
        }
    }
    while (!result.empty() && result.back() == INT_MIN) result.pop_back();
    return result;
}
TreeNode* buildFromTraversals(vector<int>& pre, int ps, int pe, int is2, int ie, unordered_map<int,int>& inMap) {
    if (ps > pe) return nullptr;
    TreeNode* root = new TreeNode(pre[ps]);
    int inIdx = inMap[pre[ps]];
    int leftSize = inIdx - is2;
    root->left = buildFromTraversals(pre, ps+1, ps+leftSize, is2, inIdx-1, inMap);
    root->right = buildFromTraversals(pre, ps+leftSize+1, pe, inIdx+1, ie, inMap);
    return root;
}
vector<int> solve(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.empty()) return {};
    unordered_map<int,int> inMap;
    for (int i = 0; i < (int)inorder.size(); i++) inMap[inorder[i]] = i;
    TreeNode* root = buildFromTraversals(preorder, 0, preorder.size()-1, 0, inorder.size()-1, inMap);
    return treeToList(root);
}

int main() { return 0; }
