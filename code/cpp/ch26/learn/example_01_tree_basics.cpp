/*
 * Example 01: Tree Basics — Traversals, Height, and More
 * Chapter 26: Trees — Branches of Logic
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <string>
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

void inorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);
    inorder(node->right, res);
}

void preorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    res.push_back(node->val);
    preorder(node->left, res);
    preorder(node->right, res);
}

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}

int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

void printVec(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i) cout << ",";
        cout << v[i];
    }
    cout << "]";
}

int main() {
    // N = INT_MIN sentinel for null
    int N = INT_MIN;
    TreeNode* tree = buildTree({1, 2, 3, 4, 5});
    vector<int> in_res, pre_res;
    inorder(tree, in_res);
    preorder(tree, pre_res);
    cout << "Inorder:   "; printVec(in_res); cout << endl;
    cout << "Preorder:  "; printVec(pre_res); cout << endl;
    cout << "Max depth: " << maxDepth(tree) << endl;
    return 0;
}
