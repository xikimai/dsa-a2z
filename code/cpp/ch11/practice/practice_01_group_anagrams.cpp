/*
 * Practice 1: Group Anagrams
 * ===========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of strings, group the anagrams together.
 *   Each inner group should be sorted alphabetically.
 *   The outer list should be sorted by the first element of each group.
 *
 * EXAMPLES:
 *   solve({"eat","tea","tan","ate","nat","bat"})
 *       -> {{"ate","eat","tea"},{"bat"},{"nat","tan"}}
 *   solve({""})  -> {{""}}
 *   solve({"a"}) -> {{"a"}}
 *
 * CONSTRAINTS:
 *   - 0 <= strs.size() <= 10^4
 *   - 0 <= strs[i].length() <= 100
 *   - strs[i] contains only lowercase English letters
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<vector<string>> solve(vector<string> strs) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<string> strs(n);
    for (int i = 0; i < n; i++) cin >> strs[i];
    vector<vector<string>> result = solve(strs);
    for (auto& group : result) {
        for (int i = 0; i < (int)group.size(); i++) {
            if (i > 0) cout << ",";
            cout << group[i];
        }
        cout << endl;
    }
    return 0;
}
