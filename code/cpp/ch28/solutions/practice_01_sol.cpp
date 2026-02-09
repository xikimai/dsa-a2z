/*
 * Solution for Practice 1: Alien Dictionary
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string solve(vector<string>& words) {
    unordered_set<char> chars;
    for (auto& w : words)
        for (char c : w) chars.insert(c);

    unordered_map<char, unordered_set<char>> adj;
    unordered_map<char, int> inDeg;
    for (char c : chars) inDeg[c] = 0;

    for (int i = 0; i < (int)words.size() - 1; i++) {
        string& w1 = words[i];
        string& w2 = words[i + 1];
        if (w1.size() > w2.size() && w1.substr(0, w2.size()) == w2) return "";
        int len = min(w1.size(), w2.size());
        for (int j = 0; j < len; j++) {
            if (w1[j] != w2[j]) {
                if (!adj[w1[j]].count(w2[j])) {
                    adj[w1[j]].insert(w2[j]);
                    inDeg[w2[j]]++;
                }
                break;
            }
        }
    }

    queue<char> q;
    for (char c : chars)
        if (inDeg[c] == 0) q.push(c);

    string result;
    while (!q.empty()) {
        char c = q.front(); q.pop();
        result += c;
        for (char nxt : adj[c])
            if (--inDeg[nxt] == 0) q.push(nxt);
    }
    return result.size() == chars.size() ? result : "";
}

int main() { return 0; }
