/*
 * Practice 5: Longest Common Prefix
 * ==================================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a vector of strings, find the longest common prefix.
 *   If there is no common prefix, return an empty string.
 *
 * EXAMPLES:
 *   solve({"flower", "flow", "flight"}) -> "fl"
 *   solve({"dog", "racecar", "car"})    -> ""
 *   solve({"abc"})                      -> "abc"
 *
 * CONSTRAINTS:
 *   - 1 <= strs.size() <= 200
 *   - 0 <= strs[i].length() <= 200
 *   - strs[i] contains only lowercase English letters
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Returns the longest common prefix of all strings.
 */
string solve(vector<string>& strs) {
    // TODO: Replace this with your solution
    return "";
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
