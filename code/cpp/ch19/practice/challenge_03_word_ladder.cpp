/*
 * Challenge 3: Word Ladder
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find shortest transformation from beginWord to endWord.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(string beginWord, string endWord, vector<string>& wordList) {
    // TODO: Replace this with your solution
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
