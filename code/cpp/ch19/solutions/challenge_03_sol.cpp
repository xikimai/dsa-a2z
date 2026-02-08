#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(string beginWord, string endWord, vector<string>& wordList) {
    unordered_set<string> wordSet(wordList.begin(), wordList.end());
    if (!wordSet.count(endWord)) return 0;

    queue<pair<string, int>> q;
    q.push({beginWord, 1});
    unordered_set<string> visited;
    visited.insert(beginWord);

    while (!q.empty()) {
        auto [word, length] = q.front(); q.pop();
        if (word == endWord) return length;
        for (int i = 0; i < (int)word.size(); i++) {
            char original = word[i];
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == original) continue;
                word[i] = c;
                if (wordSet.count(word) && !visited.count(word)) {
                    visited.insert(word);
                    q.push({word, length + 1});
                }
            }
            word[i] = original;
        }
    }
    return 0;
}

int main() {
    string beginWord, endWord;
    cin >> beginWord >> endWord;
    int n; cin >> n;
    vector<string> wordList(n);
    for (int i = 0; i < n; i++) cin >> wordList[i];
    cout << solve(beginWord, endWord, wordList) << endl;
    return 0;
}
