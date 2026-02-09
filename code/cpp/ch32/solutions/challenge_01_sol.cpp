/*
 * Solution for Challenge 1: Word Search II (Trie + Backtracking)
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    string word;
};

void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node,
         vector<string>& result, int rows, int cols) {
    char ch = board[r][c];
    if (ch == '.' || !node->children[ch - 'a']) return;

    TrieNode* next = node->children[ch - 'a'];
    if (!next->word.empty()) {
        result.push_back(next->word);
        next->word.clear(); // avoid duplicates
    }

    board[r][c] = '.';
    int dirs[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (auto& d : dirs) {
        int nr = r + d[0], nc = c + d[1];
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] != '.')
            dfs(board, nr, nc, next, result, rows, cols);
    }
    board[r][c] = ch;
}

vector<string> solve(vector<vector<char>>& board, vector<string>& words) {
    TrieNode* root = new TrieNode();
    for (auto& word : words) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->word = word;
    }

    int rows = board.size(), cols = board[0].size();
    vector<string> result;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            dfs(board, r, c, root, result, rows, cols);

    sort(result.begin(), result.end());
    return result;
}

int main() { return 0; }
