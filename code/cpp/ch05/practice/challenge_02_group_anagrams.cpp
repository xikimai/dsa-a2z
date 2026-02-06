/*
 * Challenge 2: Group Anagrams
 * ============================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a vector of strings, group the anagrams together.
 *   Each group should be sorted alphabetically, and the groups
 *   themselves should be sorted by their first element.
 *
 * EXAMPLES:
 *   solve({"eat","tea","tan","ate","nat","bat"})
 *     -> {{"ate","eat","tea"}, {"bat"}, {"nat","tan"}}
 *
 *   solve({"a"}) -> {{"a"}}
 *   solve({""})  -> {{""}}
 *
 * CONSTRAINTS:
 *   - 1 <= strs.size() <= 10^4
 *   - 0 <= strs[i].length() <= 100
 *   - strs[i] contains only lowercase English letters
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Groups anagrams together. Inner groups sorted, outer sorted by first element.
 */
vector<vector<string>> solve(vector<string>& strs) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cin.ignore();
    vector<string> strs(n);
    for (int i = 0; i < n; i++) getline(cin, strs[i]);
    vector<vector<string>> result = solve(strs);
    for (const auto& group : result) {
        for (int i = 0; i < (int)group.size(); i++) {
            if (i > 0) cout << " ";
            cout << group[i];
        }
        cout << endl;
    }
    return 0;
}
