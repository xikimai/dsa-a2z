/*
 * Solution -- Practice 5: Longest Common Prefix
 * ===============================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Compare characters column by column across all strings. Start at
 *   index 0 and check if all strings have the same character at that
 *   position. Stop when a mismatch is found or any string ends.
 *
 * TIME COMPLEXITY:  O(S) where S = sum of all characters in all strings
 * SPACE COMPLEXITY: O(1) extra
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solve(vector<string>& strs) {
    if (strs.empty()) return "";

    for (int i = 0; i < (int)strs[0].size(); i++) {
        char c = strs[0][i];
        for (int j = 1; j < (int)strs.size(); j++) {
            if (i >= (int)strs[j].size() || strs[j][i] != c) {
                return strs[0].substr(0, i);
            }
        }
    }
    return strs[0];
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cin.ignore();
    vector<string> strs(n);
    for (int i = 0; i < n; i++) getline(cin, strs[i]);
    cout << solve(strs) << endl;
    return 0;
}
