/*
 * Tests for Chapter 26: Trees — Branches of Logic
 * Build: g++ -std=c++17 -o /tmp/test_ch26 code/cpp/ch26/tests/test_ch26.cpp && /tmp/test_ch26
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Tree infrastructure
// =====================================================================

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

const int N = INT_MIN; // null sentinel

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Inorder Traversal
vector<int> ref_inorder(TreeNode* root) {
    vector<int> res;
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return;
        dfs(node->left);
        res.push_back(node->val);
        dfs(node->right);
    };
    dfs(root);
    return res;
}

// W2: Preorder Traversal
vector<int> ref_preorder(TreeNode* root) {
    vector<int> res;
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return;
        res.push_back(node->val);
        dfs(node->left);
        dfs(node->right);
    };
    dfs(root);
    return res;
}

// W3: Level Order Traversal
vector<vector<int>> ref_level_order(TreeNode* root) {
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

// W4: Maximum Depth
int ref_max_depth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(ref_max_depth(root->left), ref_max_depth(root->right));
}

// W5: Symmetric Tree
bool ref_is_mirror(TreeNode* l, TreeNode* r) {
    if (!l && !r) return true;
    if (!l || !r) return false;
    return l->val == r->val && ref_is_mirror(l->left, r->right) && ref_is_mirror(l->right, r->left);
}
bool ref_symmetric(TreeNode* root) {
    if (!root) return true;
    return ref_is_mirror(root->left, root->right);
}

// P1: Diameter
int ref_diameter_val;
int ref_height(TreeNode* node) {
    if (!node) return 0;
    int lh = ref_height(node->left);
    int rh = ref_height(node->right);
    ref_diameter_val = max(ref_diameter_val, lh + rh);
    return 1 + max(lh, rh);
}
int ref_diameter(TreeNode* root) {
    ref_diameter_val = 0;
    ref_height(root);
    return ref_diameter_val;
}

// P2: Balanced
int ref_check_balance(TreeNode* node) {
    if (!node) return 0;
    int lh = ref_check_balance(node->left);
    if (lh == -1) return -1;
    int rh = ref_check_balance(node->right);
    if (rh == -1) return -1;
    if (abs(lh - rh) > 1) return -1;
    return 1 + max(lh, rh);
}
bool ref_balanced(TreeNode* root) { return ref_check_balance(root) != -1; }

// P3: Right Side View
vector<int> ref_right_view(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            TreeNode* node = q.front(); q.pop();
            if (i == sz - 1) result.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return result;
}

// P4: Validate BST
bool ref_validate(TreeNode* node, long lo, long hi) {
    if (!node) return true;
    if (node->val <= lo || node->val >= hi) return false;
    return ref_validate(node->left, lo, node->val) && ref_validate(node->right, node->val, hi);
}
bool ref_valid_bst(TreeNode* root) { return ref_validate(root, LONG_MIN, LONG_MAX); }

// P5: Kth Smallest
int ref_kth_smallest(TreeNode* root, int k) {
    int count = 0, result = 0;
    function<void(TreeNode*)> inorder = [&](TreeNode* node) {
        if (!node) return;
        inorder(node->left);
        count++;
        if (count == k) { result = node->val; return; }
        inorder(node->right);
    };
    inorder(root);
    return result;
}

// P6: LCA
TreeNode* ref_lca_helper(TreeNode* node, int p, int q) {
    if (!node) return nullptr;
    if (node->val == p || node->val == q) return node;
    TreeNode* left = ref_lca_helper(node->left, p, q);
    TreeNode* right = ref_lca_helper(node->right, p, q);
    if (left && right) return node;
    return left ? left : right;
}
int ref_lca(TreeNode* root, int p, int q) {
    TreeNode* res = ref_lca_helper(root, p, q);
    return res ? res->val : -1;
}

// P7: Maximum Path Sum
int ref_max_path_val;
int ref_max_gain(TreeNode* node) {
    if (!node) return 0;
    int left = max(ref_max_gain(node->left), 0);
    int right = max(ref_max_gain(node->right), 0);
    ref_max_path_val = max(ref_max_path_val, left + right + node->val);
    return node->val + max(left, right);
}
int ref_max_path_sum(TreeNode* root) {
    ref_max_path_val = INT_MIN;
    ref_max_gain(root);
    return ref_max_path_val;
}

// C1: Construct from Preorder+Inorder
TreeNode* ref_build_from(vector<int>& pre, int ps, int pe, int is2, int ie, unordered_map<int,int>& inMap) {
    if (ps > pe) return nullptr;
    TreeNode* root = new TreeNode(pre[ps]);
    int inIdx = inMap[pre[ps]];
    int leftSize = inIdx - is2;
    root->left = ref_build_from(pre, ps+1, ps+leftSize, is2, inIdx-1, inMap);
    root->right = ref_build_from(pre, ps+leftSize+1, pe, inIdx+1, ie, inMap);
    return root;
}
vector<int> ref_construct(vector<int> preorder, vector<int> inorder) {
    if (preorder.empty()) return {};
    unordered_map<int,int> inMap;
    for (int i = 0; i < (int)inorder.size(); i++) inMap[inorder[i]] = i;
    TreeNode* root = ref_build_from(preorder, 0, preorder.size()-1, 0, inorder.size()-1, inMap);
    return treeToList(root);
}

// C2: Serialize and Deserialize
string ref_serialize(TreeNode* root) {
    if (!root) return "";
    string result;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        if (node) {
            result += to_string(node->val) + ",";
            q.push(node->left);
            q.push(node->right);
        } else {
            result += "N,";
        }
    }
    return result;
}
TreeNode* ref_deserialize(string data) {
    if (data.empty()) return nullptr;
    vector<string> tokens;
    stringstream ss(data);
    string token;
    while (getline(ss, token, ',')) tokens.push_back(token);
    TreeNode* root = new TreeNode(stoi(tokens[0]));
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)tokens.size()) {
        TreeNode* node = q.front(); q.pop();
        if (tokens[i] != "N") {
            node->left = new TreeNode(stoi(tokens[i]));
            q.push(node->left);
        }
        i++;
        if (i < (int)tokens.size() && tokens[i] != "N") {
            node->right = new TreeNode(stoi(tokens[i]));
            q.push(node->right);
        }
        i++;
    }
    return root;
}

// C3: Boundary Traversal
bool ref_isLeaf(TreeNode* node) { return node && !node->left && !node->right; }
void ref_addLeaves(TreeNode* node, vector<int>& result) {
    if (!node) return;
    if (ref_isLeaf(node)) { result.push_back(node->val); return; }
    ref_addLeaves(node->left, result);
    ref_addLeaves(node->right, result);
}
vector<int> ref_boundary(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    if (ref_isLeaf(root)) return {root->val};
    result.push_back(root->val);
    TreeNode* node = root->left;
    while (node) {
        if (!ref_isLeaf(node)) result.push_back(node->val);
        node = node->left ? node->left : node->right;
    }
    ref_addLeaves(root, result);
    vector<int> rightBound;
    node = root->right;
    while (node) {
        if (!ref_isLeaf(node)) rightBound.push_back(node->val);
        node = node->right ? node->right : node->left;
    }
    for (int i = rightBound.size() - 1; i >= 0; i--) result.push_back(rightBound[i]);
    return result;
}

// C4: Binary Tree Cameras
int ref_cameras;
const int REF_NOT_COVERED = 0, REF_HAS_CAMERA = 1, REF_COVERED = 2;
int ref_dfs_cameras(TreeNode* node) {
    if (!node) return REF_COVERED;
    int left = ref_dfs_cameras(node->left);
    int right = ref_dfs_cameras(node->right);
    if (left == REF_NOT_COVERED || right == REF_NOT_COVERED) { ref_cameras++; return REF_HAS_CAMERA; }
    if (left == REF_HAS_CAMERA || right == REF_HAS_CAMERA) return REF_COVERED;
    return REF_NOT_COVERED;
}
int ref_min_cameras(TreeNode* root) {
    ref_cameras = 0;
    if (ref_dfs_cameras(root) == REF_NOT_COVERED) ref_cameras++;
    return ref_cameras;
}

// C5: Flatten Binary Tree
vector<int> ref_flatten(TreeNode* root) {
    vector<int> result;
    function<void(TreeNode*)> preorder = [&](TreeNode* node) {
        if (!node) return;
        result.push_back(node->val);
        preorder(node->left);
        preorder(node->right);
    };
    preorder(root);
    return result;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_bool(bool expected, bool actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) { if (i) cout << ","; cout << expected[i]; }
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) { if (i) cout << ","; cout << actual[i]; }
        cout << "]" << endl;
    }
}

void check_vec2d(vector<vector<int>> expected, vector<vector<int>> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << endl; }
}

int main() {
    cout << "Chapter 26: Trees — Branches of Logic" << endl;
    cout << "========================================" << endl << endl;

    // W1: Inorder
    check_vec({1,3,2}, ref_inorder(buildTree({1,N,2,3})), "W1: basic");
    check_vec({4,2,5,1,3}, ref_inorder(buildTree({1,2,3,4,5})), "W1: full");
    check_vec({}, ref_inorder(nullptr), "W1: empty");
    check_vec({1}, ref_inorder(buildTree({1})), "W1: single");

    // W2: Preorder
    check_vec({1,2,3}, ref_preorder(buildTree({1,N,2,3})), "W2: basic");
    check_vec({1,2,4,5,3}, ref_preorder(buildTree({1,2,3,4,5})), "W2: full");
    check_vec({}, ref_preorder(nullptr), "W2: empty");

    // W3: Level Order
    check_vec2d({{3},{9,20},{15,7}}, ref_level_order(buildTree({3,9,20,N,N,15,7})), "W3: basic");
    check_vec2d({{1}}, ref_level_order(buildTree({1})), "W3: single");
    check_vec2d({}, ref_level_order(nullptr), "W3: empty");

    // W4: Max Depth
    check(3, ref_max_depth(buildTree({3,9,20,N,N,15,7})), "W4: basic");
    check(2, ref_max_depth(buildTree({1,N,2})), "W4: skewed");
    check(0, ref_max_depth(nullptr), "W4: empty");

    // W5: Symmetric
    check_bool(true, ref_symmetric(buildTree({1,2,2,3,4,4,3})), "W5: symmetric");
    check_bool(false, ref_symmetric(buildTree({1,2,2,N,3,N,3})), "W5: asymmetric");
    check_bool(true, ref_symmetric(nullptr), "W5: empty");

    // P1: Diameter
    check(3, ref_diameter(buildTree({1,2,3,4,5})), "P1: basic");
    check(1, ref_diameter(buildTree({1,2})), "P1: two");
    check(0, ref_diameter(nullptr), "P1: empty");

    // P2: Balanced
    check_bool(true, ref_balanced(buildTree({3,9,20,N,N,15,7})), "P2: balanced");
    check_bool(false, ref_balanced(buildTree({1,2,2,3,3,N,N,4,4})), "P2: unbalanced");
    check_bool(true, ref_balanced(nullptr), "P2: empty");

    // P3: Right Side View
    check_vec({1,3,4}, ref_right_view(buildTree({1,2,3,N,5,N,4})), "P3: basic");
    check_vec({1,3}, ref_right_view(buildTree({1,N,3})), "P3: right skewed");
    check_vec({}, ref_right_view(nullptr), "P3: empty");

    // P4: Validate BST
    check_bool(true, ref_valid_bst(buildTree({2,1,3})), "P4: valid");
    check_bool(false, ref_valid_bst(buildTree({5,1,4,N,N,3,6})), "P4: invalid");
    check_bool(true, ref_valid_bst(buildTree({1})), "P4: single");

    // P5: Kth Smallest
    check(1, ref_kth_smallest(buildTree({3,1,4,N,2}), 1), "P5: first");
    check(3, ref_kth_smallest(buildTree({5,3,6,2,4,N,N,1}), 3), "P5: third");

    // P6: LCA
    check(3, ref_lca(buildTree({3,5,1,6,2,0,8,N,N,7,4}), 5, 1), "P6: root");
    check(5, ref_lca(buildTree({3,5,1,6,2,0,8,N,N,7,4}), 5, 4), "P6: ancestor");
    check(1, ref_lca(buildTree({1,2}), 1, 2), "P6: parent-child");

    // P7: Max Path Sum
    check(6, ref_max_path_sum(buildTree({1,2,3})), "P7: basic");
    check(42, ref_max_path_sum(buildTree({-10,9,20,N,N,15,7})), "P7: negative");
    check(-3, ref_max_path_sum(buildTree({-3})), "P7: single negative");

    // C1: Construct from Preorder+Inorder
    check_vec({3,9,20,N,N,15,7}, ref_construct({3,9,20,15,7}, {9,3,15,20,7}), "C1: basic");
    check_vec({-1}, ref_construct({-1}, {-1}), "C1: single");

    // C2: Serialize/Deserialize (round-trip)
    {
        TreeNode* tree = buildTree({1,2,3,N,N,4,5});
        string s = ref_serialize(tree);
        TreeNode* restored = ref_deserialize(s);
        string s2 = ref_serialize(restored);
        if (s == s2) { passed++; } else { failed_count++; cout << "FAIL: C2: round-trip" << endl; }

        string empty = ref_serialize(nullptr);
        TreeNode* nullTree = ref_deserialize(empty);
        if (nullTree == nullptr) { passed++; } else { failed_count++; cout << "FAIL: C2: empty" << endl; }
    }

    // C3: Boundary Traversal
    check_vec({1,2,4,7,8,9,10,6,3}, ref_boundary(buildTree({1,2,3,4,5,6,N,N,N,7,8,9,10})), "C3: basic");
    check_vec({1}, ref_boundary(buildTree({1})), "C3: single");

    // C4: Binary Tree Cameras
    check(1, ref_min_cameras(buildTree({0,0,N,0,0})), "C4: basic");
    check(2, ref_min_cameras(buildTree({0,0,N,0,N,0,N,N,0})), "C4: longer");

    // C5: Flatten Binary Tree
    check_vec({1,2,3,4,5,6}, ref_flatten(buildTree({1,2,5,3,4,N,6})), "C5: basic");
    check_vec({}, ref_flatten(nullptr), "C5: empty");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch26 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_count);
        return 1;
    }
    return 0;
}
