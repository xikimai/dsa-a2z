/*
 * Solution for Warmup 1: Trie Insert and Search
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    bool isEnd = false;
};

vector<bool> solve(vector<string>& words, vector<string>& queries) {
    TrieNode* root = new TrieNode();
    for (auto& word : words) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }
    vector<bool> result;
    for (auto& q : queries) {
        TrieNode* node = root;
        bool found = true;
        for (char ch : q) {
            int idx = ch - 'a';
            if (!node->children[idx]) { found = false; break; }
            node = node->children[idx];
        }
        result.push_back(found && node->isEnd);
    }
    return result;
}

int main() { return 0; }
