/*
 * Example 01: Trie Basics — Building a Prefix Tree
 * Chapter 32: String Algorithms — Beyond Brute Force
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    bool isEnd = false;
    int prefixCount = 0;
};

class Trie {
    TrieNode* root = new TrieNode();
public:
    void insert(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
            node->prefixCount++;
        }
        node->isEnd = true;
    }

    bool search(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }

    int startsWith(const string& prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            int idx = ch - 'a';
            if (!node->children[idx]) return 0;
            node = node->children[idx];
        }
        return node->prefixCount;
    }
};

int main() {
    cout << "TRIE BASICS" << endl;
    Trie trie;
    vector<string> words = {"apple", "app", "application", "apt", "banana"};
    for (auto& w : words) trie.insert(w);

    cout << "  search('app') = " << trie.search("app") << endl;
    cout << "  search('ban') = " << trie.search("ban") << endl;
    cout << "  startsWith('app') = " << trie.startsWith("app") << endl;
    cout << "  startsWith('a') = " << trie.startsWith("a") << endl;
    return 0;
}
