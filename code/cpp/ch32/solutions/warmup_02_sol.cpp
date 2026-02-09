/*
 * Solution for Warmup 2: Trie Prefix Count
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    int count = 0;
};

vector<int> solve(vector<string>& words, vector<string>& prefixes) {
    TrieNode* root = new TrieNode();
    for (auto& word : words) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
            node->count++;
        }
    }
    vector<int> result;
    for (auto& prefix : prefixes) {
        TrieNode* node = root;
        bool found = true;
        for (char ch : prefix) {
            int idx = ch - 'a';
            if (!node->children[idx]) { found = false; break; }
            node = node->children[idx];
        }
        result.push_back(found ? node->count : 0);
    }
    return result;
}

int main() { return 0; }
